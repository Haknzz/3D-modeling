# ChatGPT — Modelagem 3D e Animações

Skill para orientar um assistente na criação e no refinamento de modelos 3D, preparar animações e apresentar prévias de acordo com o objetivo de cada usuário. Pode ser usada em jogos, visualização de produtos, móveis, personagens, veículos, protótipos e demonstrações.

## Para que serve

- Modelar personagens, veículos e objetos a partir de referências visuais.
- Preparar rigs e adaptar animações, incluindo arquivos do Mixamo quando disponíveis.
- Corrigir movimentos rígidos, apoio dos pés, pegada das mãos e transições.
- Animar saltos, transporte de caixas, carga e descarga e movimentos de veículos.
- Conferir escala, materiais e enquadramento em uma prévia 3D interativa.
- Separar a revisão visual da exportação e da integração no motor do jogo.

A skill fornece instruções e um verificador de trajetórias. Ela não inclui modelos prontos, uma biblioteca de animações ou um serviço automático de geração 3D. O resultado depende das ferramentas de modelagem, execução e visualização disponíveis ao assistente.

## Escopo e personalização

A skill não fixa um tema militar, um estilo visual ou um projeto. Cada usuário define o objeto, a referência, o estilo, as ações e o formato de entrega. As instruções são voltadas a modelagem, animação e visualização 3D; não substituem skills de assuntos sem relação com 3D.

## Como usar

No assistente que tiver a skill instalada, mencione `$modelar-visualizar-3d` e descreva o modelo, a ação e o resultado desejado. Anexe as referências e arquivos-base quando houver.

Exemplos:

> Use $modelar-visualizar-3d para criar uma cadeira inspirada nesta foto e mostrar uma prévia 3D que permita girar e observar os detalhes.

> Use $modelar-visualizar-3d para criar um robô com animações de caminhada e corrigir o apoio dos pés e as transições.

> Use $modelar-visualizar-3d para animar um personagem pegando um objeto, transportando-o e apoiando-o sobre uma mesa, com movimentos naturais.

Para instalar, forneça a pasta **chatgpt** completa a um assistente com suporte a skills e solicite a instalação. O arquivo de instruções executáveis permanece com o nome **SKILL.md**, exigido pelo formato; **chatgpt.md** é o guia de apresentação desta versão. Preservar os arquivos e caminhos relativos da pasta é necessário para acessar suas referências e seu script.

## Arquivos

A pasta [chatgpt](chatgpt) contém:

- [SKILL.md](chatgpt/SKILL.md): fluxo principal de modelagem, animação, revisão e entrega.
- `agents/openai.yaml`: nome, descrição e configuração da skill.
- `references/movimento-e-contatos.md`: orientações para rig, passadas, saltos e manipulação de objetos.
- `references/previa-e-entrega.md`: visualização, validação e formatos de entrega.
- `scripts/validar_movimento.py`: verificação de trajetórias declaradas em metros.
- `assets/icon.svg`: ícone da skill.

## Verificador de movimento

O script usa somente a biblioteca padrão do Python 3. Executar:

```sh
python3 chatgpt/scripts/validar_movimento.py trajetorias.json
```

O JSON deve conter nomes das juntas, índices dos pais e quadros com tempo, posições e contatos. O esquema está documentado no início do script. As tolerâncias padrão são 1,5 cm para contatos e 0,5% para variação dos comprimentos dos ossos; podem ser alteradas com `--contact-tol` e `--bone-tol`.

Saída: relatório JSON e código 0 quando as verificações passam, 1 quando há falhas e 2 quando a entrada é inválida. O verificador não avalia qualidade artística, colisões da malha ou naturalidade do movimento; esses aspectos exigem inspeção visual.

## Entrega e integração

Uma prévia HTML ou um pacote de fontes não equivale a um arquivo GLB/FBX importável. Solicitar a exportação e a validação no motor desejado quando forem necessárias. A skill orienta a integrar ao jogo apenas quando essa etapa for solicitada.

## Compatibilidade

Esta versão foi criada com o ChatGPT. As instruções também podem ser adaptadas para outros assistentes; a prévia interativa depende dos recursos do ambiente. O verificador roda separadamente em Python 3. A skill não é um produto oficial da OpenAI e não inclui código, modelos, mapas ou arquivos privados de projetos.
