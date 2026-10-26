---
name: amazoning-motion-studies
description: Criar poses originais, estudos de movimento e construção anatômica em perspectiva preservando a identidade dos personagens de AMAZONING. Usar em conjunto com amazoning-art-direction.
---

# Movimento e construção com preservação de identidade

## Escopo e fontes

Leia `AGENTS.md`, a skill `amazoning-art-direction`, a ficha do personagem, o registro de decisões e o inventário de imagens-mestras. Abra a imagem-mestra; não basta conhecer seu caminho. Não escolha outra imagem como oficial por conta própria. Preserve todas as características documentadas e visualmente verificáveis; esta skill não autoriza alterar cânone.

Uma skill orienta a geração e a inspeção, mas não garante fidelidade automática. Uma geração bonita com máscara ou figurino divergente falha na revisão.

## Separe identidade de movimento

- Identidade: referência aprovada do personagem e ficha; determina rosto, cabelo, máscara, silhueta, paleta e peças do traje.
- Movimento: referências de gesto, equilíbrio, enquadramento e perspectiva; não determinam a identidade.
- Construção: caixas de cabeça, tórax e pélvis; cilindros com elipses de seção para membros; articulações e blocos para mãos e pés.

Quando solicitadas, referências como Jujutsu Kaisen podem informar ritmo de combate, antecipação, torção e escorço; Death Stranding pode informar transferência de peso, equilíbrio e resposta corporal ao terreno. Essas são direções de estudo, não descrições oficiais dessas obras. Não importar rostos, uniformes, símbolos, equipamentos ou personagens para AMAZONING. Não adicionar carga ou mochila ao personagem só porque a referência de movimento usa uma. Desenvolva poses próprias, sem copiar uma prancha inteira.

## Trava de identidade antes da geração

Prepare uma tabela com atributo, fonte, classificação (confirmado/estimado/pendente), restrição e teste visual. Use os sete grupos da skill de direção de arte. Para máscara, acrescente uma conferência dedicada:

- Contorno externo, recortes diagonais e limites sobre nariz e bochechas.
- Quantidade, formato e inclinação das aberturas dos olhos.
- Ponte nasal, laterais, espessura aparente, peças e fixações visíveis.
- Relação entre máscara e gola: são peças distintas; não fundi-las.
- Cor e materiais observáveis, sem inventar hexadecimais ou geometria de partes ocultas.

Use o detalhe da máscara na imagem-mestra como referência de inspeção. Não troque máscara por óculos, visor, faixa ou modelo genérico. Partes não mostradas permanecem não verificáveis, sem serem aprovadas por inferência. Peça esclarecimento somente se a ambiguidade impedir a pose escolhida; caso contrário, escolha um ângulo documentado.

## Briefing de pose

Defina ação, intenção, fase do movimento, apoio, direção da força, linha de ação, câmera e contato com o chão. Para uma sequência, mantenha trajetória e continuidade entre antecipação, ação e recuperação. Identifique propostas de movimento como estudos; não crie poderes ou habilidades canônicas.

Exemplos de estudos: esquiva com pivô e rotação do tronco; avanço com mão em escorço; recuperação de equilíbrio em declive sem equipamento adicional. Escolha gestos compatíveis com o personagem.

## Perspectiva e anatomia

Use uma câmera coerente por quadro. Marque horizonte e pontos de fuga que realmente correspondam à grade; horizonte é o nível da câmera, não uma linha decorativa na base. Não misture câmeras de quadros independentes numa grade única. Desenhe arestas ocultas tracejadas e mantenha as elipses orientadas ao eixo de cada cilindro. Verifique inserção dos membros, lateralidade, número de dedos, apoio e centro de massa.

Se apresentar versão vestida e manequim correspondente, compare a mesma pose, câmera, articulações e contatos com o chão. Mantenha as linhas estruturais legíveis e não as use para esconder defeitos do traje.

## Geração e revisão

1. Use a imagem-mestra disponível como referência visual da ferramenta. Descreva as referências de movimento separadamente. Para corrigir arte existente, forneça também a candidata defeituosa quando disponível e diga quais regiões corrigir.
2. Trabalhe primeiro com uma pose legível e um detalhe de rosto/máscara. Expanda somente após revisar os atributos de identidade.
3. Abra a saída e compare lado a lado com a imagem-mestra. Preencha os sete grupos e a conferência da máscara com `conforme`, `divergente` ou `não verificável`. Não chame um item de conforme apenas porque estava no prompt.
4. Se houver divergência visível, faça uma edição localizada preservando as regiões corretas. Reabra e revise o resultado. Se a correção continuar falhando, registre a limitação e entregue apenas como estudo com divergências; não declare preservação integral.
5. Não prometa equivalência exata de pixels em uma pose nova gerada. Preserve o design verificável e sinalize detalhes pequenos que não possam ser conferidos na resolução disponível.

## Arquivos e entrega

Salve versões distintas em `assets/concept-art/<personagem>/`, sem sobrescrever a mestra nem a candidata anterior. Use nomes como `<personagem>_estudo_movimento_v02_candidata.png`. Salve um relatório Markdown associado com fontes, intenção, matriz antes/depois, divergências e operações realizadas. Registre a candidata no inventário sem alterar designações oficiais. Não aplique logotipo gerado; siga a skill de direção de arte se a marca for necessária.

Status inicial: **CANDIDATA — NÃO APROVADA**. O pedido de gerar, salvar ou fazer push não aprova a imagem como referência oficial. Informe os caminhos e forneça acesso verificável ao arquivo; não repita links internos como se fossem downloads públicos. Push somente quando autorizado na conversa.
