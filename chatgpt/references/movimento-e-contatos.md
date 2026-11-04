# Movimento, contato e naturalidade

## Rig e cinemática

Usar transformações locais para interpolar rotações, com quaternions normalizados e sinais consistentes entre amostras. Reconstituir o mundo por FK; obter skinning com `world[junta] × inverse_bind[junta]`. Não interpolar matrizes acumuladas como solução de autoria. Na reprodução, interpolar transformações locais por rotação e translação quando possível; avaliar o erro se usar interpolação linear de paletas de skin.

Resolver dois segmentos mantendo seus comprimentos. Para alvo a distância d, usar alcance limitado a L1 + L2 − margem e a lei dos cossenos para posicionar o cotovelo/joelho. Usar um vetor de orientação explícito para o plano de dobra. Reportar o erro entre a extremidade resolvida e o alvo original; limitar o alvo não autoriza reportar erro zero. Ajustar pelve ou posição do objeto quando o alcance for insuficiente.

Posicionar a mão no punho e orientar palma e dedos pela superfície e alça do objeto. Evitar braços cruzados por confusão entre esquerda do personagem e esquerda da câmera. Incluir dedos que envolvam a alça quando o enquadramento os tornar visíveis.

## Passadas e giros

- Manter apoios em coordenadas do chão durante a fase de suporte, inclusive quando a pelve se desloca.
- Planejar trajetórias de balanço do pé com altura suficiente, posição inicial/final e transferência de peso.
- Sincronizar braços e tronco com a fase dos pés, não com um seno independente do tempo global.
- Evitar pernas quase travadas em toda a marcha; flexionar joelhos e controlar altura e oscilação da pelve.
- Iniciar um giro com olhar e tronco e completá-lo com passos. Preservar a posição de apoio durante a rotação; não girar os dois pés deslizando ao mesmo tempo.
- Não usar uma sequência de agachamentos como substituto de caminhar com peso.

## Saltar de uma superfície elevada

1. Aproximar o corpo da borda sem atravessar tampa, lona ou chassi.
2. Antecipar com transferência de peso, joelhos flexionados e braços preparados. Ligar a posição final da antecipação à primeira pose da fase aérea sem saltos de pelve ou mãos.
3. Definir a fase aérea pelo centro de massa e gravidade. Uma trajetória de referência é `y(t)=y0+v0*t−g*t²/2`; adequar o tempo e a velocidade ao desnível e ao estilo do jogo. Não aplicar smoothstep à queda completa.
4. Flexionar as pernas e usar braços para equilíbrio sem esticar os segmentos. Manter espaço livre entre corpo e carroceria.
5. Detectar o primeiro contato das solas; amortecer com tornozelos, joelhos, pelve e tronco. Manter os pés apoiados durante a compressão e a recuperação.
6. Passar a caminhar somente após recuperar o apoio. Não inventar escada ou degraus quando o pedido for removê-los.

## Carregar e descarregar caixas

Planejar o local inicial, a área de trabalho e o apoio final de cada caixa. Evitar interseção com as outras caixas e com o caminhão. Fazer o personagem alcançar a caixa, estabelecer a pegada, transferir o peso e só então levantar. Manter a carga próxima ao corpo durante o transporte e orientar os passos para o destino.

Na entrega, apoiar primeiro a caixa no chão ou no piso real da carroceria, liberar os dedos e recuar as mãos depois. Conferir a altura da superfície pela geometria efetiva, e não por um número herdado de uma plataforma removida.

Separar abrir lona, abrir tampa e transferir carga. Se o personagem fechar a lona do chão, modelar uma fita/corda ou mecanismo alcançável e animar a pegada correspondente. Não fazer braços alcançarem um ponto fisicamente fora do alcance.

## Veículos e efeitos

Relacionar rotação das rodas à distância percorrida e ao raio, com sinal coerente na ré. Aplicar direção apenas nos eixos que esterçam e aproximar a geometria de curva das rodas interna e externa. Separar suspensão de rotação das rodas e manter carga apoiada na carroceria.

Em disparos, sincronizar projétil, chama, fumaça e reação do corpo com um evento único. Prender efeitos a sockets; não emitir de um ponto fixo fora do cano. Não inventar especificações de armamento real para justificar efeitos de jogo.
