#!/usr/bin/env python3
"""Validar trajetórias em metros; não avaliar estética nem colisões da malha.
Entrada JSON: {"names":["hip","hand"], "parents":[-1,0], "frames":[
 {"time":0,"joints":[[0,0,0],[1,0,0]],"contacts":[
 {"joint":"hand","target":[1,0,0],"kind":"hand"}]}]}.
Contatos são alvos declarados de extremidades, não prova de aderência da malha.
"""
import argparse
import json
import math
from pathlib import Path


def distance(a, b):
    return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))


def validate(data, contact_tol=.015, bone_tol=.005):
    names, parents, frames = data['names'], data['parents'], data['frames']
    if not names or len(names) != len(parents) or not frames:
        raise ValueError('Exigir juntas, pais e pelo menos um quadro.')
    if len(set(names)) != len(names):
        raise ValueError('Nomes de juntas duplicados.')
    for i, parent in enumerate(parents):
        if not isinstance(parent, int) or parent < -1 or parent >= len(names) or parent == i:
            raise ValueError('Índice de pai inválido.')
        visited, node = set(), i
        while node >= 0:
            if node in visited:
                raise ValueError('Hierarquia cíclica.')
            visited.add(node)
            node = parents[node]
    errors, contacts, max_contact, max_bone = [], 0, 0., 0.
    baseline = None
    previous = -math.inf
    for f, frame in enumerate(frames):
        points, time = frame['joints'], frame['time']
        if not isinstance(time, (int, float)) or not math.isfinite(time) or time <= previous:
            raise ValueError('Tempos devem ser finitos e estritamente crescentes.')
        previous = time
        if len(points) != len(names) or any(len(p) != 3 or not all(math.isfinite(x) for x in p) for p in points):
            raise ValueError('Juntas devem conter três coordenadas finitas em cada quadro.')
        lengths = [distance(points[i], points[parent]) if parent >= 0 else None for i, parent in enumerate(parents)]
        if baseline is None:
            baseline = lengths
        for i, length in enumerate(lengths):
            if length is None or baseline[i] < 1e-8:
                continue
            drift = abs(length-baseline[i])/baseline[i]
            max_bone = max(max_bone, drift)
            if drift > bone_tol:
                errors.append({'frame': f, 'joint': names[i], 'issue': 'bone_length', 'relative_error': drift})
        for contact in frame.get('contacts', []):
            joint = names.index(contact['joint'])
            target = contact['target']
            if len(target) != 3 or not all(math.isfinite(x) for x in target):
                raise ValueError('Alvo de contato inválido.')
            error = distance(points[joint], target)
            contacts += 1
            max_contact = max(max_contact, error)
            if error > contact_tol:
                errors.append({'frame': f, 'joint': names[joint], 'issue': 'contact', 'error_m': error})
    return {'passed': not errors, 'frames': len(frames), 'contacts_checked': contacts,
            'max_contact_error_m': max_contact if contacts else None,
            'max_bone_relative_error': max_bone, 'issues_total': len(errors), 'issues': errors[:50],
            'scope': 'Trajetórias e contatos declarados; sem avaliação estética ou colisões.'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('input', type=Path)
    ap.add_argument('--contact-tol', type=float, default=.015)
    ap.add_argument('--bone-tol', type=float, default=.005)
    args = ap.parse_args()
    if args.contact_tol < 0 or args.bone_tol < 0:
        ap.error('Tolerâncias devem ser não negativas.')
    try:
        report = validate(json.loads(args.input.read_text()), args.contact_tol, args.bone_tol)
    except (ValueError, KeyError, TypeError, IndexError) as error:
        print(json.dumps({'passed': False, 'input_error': str(error)}, ensure_ascii=False))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
