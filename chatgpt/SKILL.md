---
name: modelar-visualizar-3d
description: Criar e refinar modelos 3D de personagens, veículos e objetos para jogos, animar ações e apresentar prévias interativas antes da integração. Usar para pedidos de modelagem com foto de referência, rig e retargeting Mixamo, animações de combate ou logística, correção de movimentos rígidos, contatos de mãos e pés, saltos, carga e descarga e inspeção visual de modelos. Não usar para substituir modelos 3D por imagens conceituais ou para integrar no jogo sem solicitação.
---

# Modelagem 3D e animações

Produzir geometria tridimensional e movimento inspecionável. Responder em português quando o usuário escrever em português. Trabalhar com o modelo existente quando houver; preservar as partes aprovadas e aplicar a mudança solicitada.

## Delimitar a entrega

- Identificar a referência, a ação, o modelo-base e o formato solicitado. Procurar os arquivos indicados nas fontes disponíveis antes de pedir reenvio.
- Distinguir prévia, pacote de fontes, exportação GLB/FBX e integração no motor. Entregar somente o que foi realmente produzido; nunca chamar um fragmento HTML ou um JSON de modelo GLB pronto para Godot.
- Assumir prévia fora do jogo quando o contexto estabelecer essa etapa. Integrar ao projeto apenas quando solicitado.
- Não inventar que uma skill, animação, modelo ou exportação já existe. Formalizar o processo como skill quando solicitado.
- Usar referências visuais para proporções, materiais, silhueta e detalhes. Criar um modelo original; não afirmar reprodução exata de um veículo real ou de um personagem de outra franquia.

## Preparar a estrutura

1. Inspecionar imagens e arquivos locais. Para FBX, confirmar hierarquia, take correto, unidades, eixos, duração e frequência. Não deduzir compatibilidade apenas pelo nome Mixamo.
2. Normalizar o espaço de trabalho em metros e registrar a conversão aplicada. Preservar inversas de bind e offsets dos filhos; evitar misturar centímetros do FBX com metros dos acessórios.
3. Separar peças rígidas articuladas: rodas, direção, esteiras, torre, tampa, lona, carga e armas. Definir pivôs nos eixos mecânicos reais.
4. Para personagens, manter uma malha contínua e rig deformável, com pesos normalizados e mãos articuladas. Preferir um rig humano existente a membros soltos construídos com blocos.
5. Modelar detalhes que alterem a leitura: bordas, costuras, bolsas, ferragens, sulcos, faróis, vidros, molas e interiores visíveis. Reutilizar malhas idênticas e manter resolução adequada à câmera do jogo.

## Construir as animações

Ler [movimento-e-contatos.md](references/movimento-e-contatos.md) antes de criar ou corrigir ações humanas, saltos ou interações com objetos.

- Organizar cada ação em antecipação, execução, contato e recuperação. Definir eventos de pegar, soltar, disparar, apoiar, tocar o chão e terminar.
- Usar interpolação suave onde o gesto pede desaceleração; não aplicar ease-in/ease-out a todos os passos ou à queda inteira. Preservar velocidade durante a passada e aceleração gravitacional na fase aérea.
- Manter o objeto preso às mãos durante o transporte e imóvel no apoio após soltar. Usar alvos locais nos pontos de pegada e resolver os dois braços sem esticar ossos.
- Fixar o pé que suporta peso. Alternar apoios, movimento da pelve, flexão do joelho e orientação do tornozelo. Adicionar balanço dos braços e contraposição do tronco sincronizados com a passada.
- Distribuir giros entre cabeça, tronco, pelve e passos. Evitar trocar o yaw do corpo instantaneamente em uma fronteira de ação.
- Usar sutileza: respiração e movimento secundário não corrigem trajetórias erradas, poses desequilibradas ou contatos falsos.
- Amostrar ações rápidas a pelo menos 30 fps e interpolar a reprodução. Aumentar a taxa somente se necessário; mais quadros não tornam uma coreografia rígida natural.
- Preservar continuidade de posição, orientação e velocidade nas transições. Incluir mudanças de estado de objetos e câmera nessa verificação.

## Apresentar a prévia

Ler [previa-e-entrega.md](references/previa-e-entrega.md) para escolher o caminho de visualização, validação e salvamento.

- Para visualização dentro da conversa, aplicar a skill de visualização disponível e seu contrato atual. Não copiar instruções internas de outro plugin para esta skill.
- Preferir visualização 3D real com seleção de ação, reproduzir/pausar, linha do tempo, giro de câmera e zoom. Incluir vista do detalhe relevante, como a traseira na logística.
- Iniciar parado e permitir reprodução voluntária. Oferecer um acesso direto à ação principal quando ela ocorrer no meio de uma sequência longa.
- Mostrar erros de carregamento de modo legível. Não apresentar um canvas vazio como entrega concluída.

## Verificar antes de entregar

1. Testar mudanças de ação, busca de quadros, início/fim, pausa, câmera e largura móvel.
2. Renderizar quadros reais de antecipação, contato, impacto e recuperação; examinar frente, lateral e traseira. Conferir também movimento contínuo quando houver um renderizador funcional.
3. Verificar caixa atravessando o tronco, arma atravessando capacete, pés no chão, clipping com carroceria, escala, orientação e acessórios.
4. Executar `scripts/validar_movimento.py` quando houver trajetórias de juntas e contatos no esquema documentado pelo próprio script. Não tratar esse teste como avaliação estética ou como teste de colisões da malha.
5. Corrigir falhas encontradas. Distinguir teste de interface com WebGL simulado de compilação/renderização real. Se não houver visualização real disponível, relatar essa limitação; não declarar qualidade visual verificada somente com mocks.
6. Salvar entregáveis conforme as capacidades de armazenamento disponíveis, mantendo a identidade de um arquivo quando atualizar sua versão. Não prometer persistência sem confirmação de salvamento.

Concluir com o que mudou, a prévia ou arquivo e a limitação material relevante. Não afirmar que algo está implementado no jogo se somente a prévia foi alterada.
