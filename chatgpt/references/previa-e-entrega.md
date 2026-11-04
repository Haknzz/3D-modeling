# Prévia e entrega

## Escolher o renderizador

Usar ferramentas disponíveis no ambiente, sem presumir Blender, Godot, navegador com WebGL ou acesso livre à rede. Para modelos procedurais ou peças articuladas, uma prévia WebGL pode agrupar a geometria por nó e aplicar matrizes por peça. Para humanos, usar skinning e rig deformável. Reutilizar rodas, caixas e acessórios idênticos para reduzir dados e chamadas.

Para prévias na conversa, seguir o contrato atual da skill de visualização quando ela estiver disponível. Usar dados embutidos e bibliotecas permitidas pela superfície. Se não houver capacidade de visualização inline, entregar um HTML independente ou um vídeo renderizado e dizer como abri-lo. Não inventar uma sintaxe de widget indisponível.

## Validação visual e de interface

Verificar erros JavaScript, atributos finitos, materiais, shaders e interação. Um mock permite verificar eventos de interface, mas não prova que shaders compilam, que a malha aparece ou que o movimento é natural.

Preferir renderização real do mesmo modelo e das mesmas transformações da prévia. Se WebGL não estiver disponível no navegador local, considerar um renderizador EGL/GLES ou outro renderizador acessível e registrar a diferença. Observar quadros de contato e transição, e não apenas o ponto médio de cada ação.

Verificar enquadramento para personagem e acessórios no ponto mais alto e mais distante. Dar acesso à área da ação: traseira e interior do caminhão para logística; lado do ombro para lançadores. Preservar controles legíveis em telas estreitas.

## Formatos e fidelidade

- Prévia interativa: permitir revisão visual; não afirmar compatibilidade de importação no motor.
- Fontes e dados: incluir geometria, rig ou hierarquia, materiais, catálogo e scripts necessários. Informar dependências externas; evitar caminhos absolutos do ambiente de autoria.
- GLB/FBX: produzir bytes reais, reabrir e conferir hierarquia, escala, materiais, duração e canais. Validar no motor alvo antes de declarar integração concluída.
- Efeitos de shader ou partículas exclusivos da prévia podem precisar de implementação própria no motor; declarar quais não foram exportados.

Salvar e versionar somente os entregáveis solicitados ou necessários. Usar o mecanismo de armazenamento vigente; manter a identidade de arquivos existentes nas revisões. Guardar ferramentas internas e renderizações intermediárias separadas do pacote entregue. Não incluir modelos ou imagens privados de outro usuário ao compartilhar a skill.
