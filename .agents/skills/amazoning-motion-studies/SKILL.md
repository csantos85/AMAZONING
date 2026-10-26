---
name: amazoning-motion-studies
description: Criar poses originais, estudos de movimento e construção anatômica em perspectiva preservando a identidade dos personagens de AMAZONING. Usar em conjunto com amazoning-art-direction.
---

# Movimento e construção com preservação de identidade

## Escopo e fontes

Leia `AGENTS.md`, a skill `amazoning-art-direction`, a ficha do personagem, o registro de decisões e o inventário de imagens-mestras. Abra a imagem-mestra; não basta conhecer seu caminho. Não escolha outra imagem como oficial por conta própria. Preserve todas as características documentadas e visualmente verificáveis; esta skill não autoriza alterar cânone.

Uma skill orienta a geração e a inspeção, mas não garante fidelidade automática. Uma geração bonita com máscara ou figurino divergente falha na revisão.

## Preservação integral obrigatória

Requisito explícito do criador: diferenças físicas entre versões não são aceitáveis. Este requisito prevalece sobre os procedimentos exploratórios abaixo. Não apresentar geração livre, mesmo condicionada por referência ou seed, como solução determinística de identidade. Não entregar uma versão divergente como cumprimento do pedido, nem contornar a exigência chamando-a apenas de candidata. Estudos anteriores com divergências são histórico, não fontes de anatomia.

Escolha o procedimento conforme o resultado necessário:

1. **Mesma pose da imagem-base:** preservar a imagem original intacta e adicionar construção em camada separada, sem regenerar, retocar, deformar ou recolorir o personagem. Guardar o original e seu hash. Verificar que a camada do personagem contém os mesmos pixels antes da composição. As linhas estruturais são interpretações didáticas e não revelam medidas ocultas reais. Não alegar identidade de pixels da composição final quando houver linhas por cima; a identidade se refere à camada original preservada.
2. **Nova pose ou câmera:** exigir um ativo mestre articulável aprovado (modelo/rig 3D ou rig 2D dentro dos ângulos documentados). A imagem-base isolada não determina anatomia, medidas, profundidade ou superfícies ocultas de forma única. Sem esse ativo, preparar especificação e estudos de manequim independentes, mas não gerar novas versões finais do personagem sob promessa de preservação integral.
3. **Construção do ativo mestre:** é uma etapa de interpretação e aprovação, não reprodução automática garantida. Documentar vistas e dimensões ainda desconhecidas; obter decisões para as lacunas antes de considerá-las oficiais. Um rig 2D não autoriza inventar ângulos fora de seu escopo aprovado.

Para um ativo aprovado, fixar versão e hashes de malha, topologia, proporções, materiais/texturas, máscara, cabelo, figurino e rig. Permitir somente poses/câmeras e deformações previstas pelo rig; impedir edição de forma, escalas ósseas e morphs de identidade. Registrar unidades, comprimentos ósseos, escala, parâmetros de deformação, câmera, iluminação, motor, versões e configurações de render. Comparar hashes e parâmetros com a linha de base; alterações de pose previstas são declaradas separadamente dos dados imutáveis. Validar deformações em poses extremas, inclusive volume, articulações e relações faciais, com tolerâncias documentadas e aprovadas, sem inventar limites para fazer passar.

Repetibilidade de render deve ser testada no ambiente fixado; não presumir equivalência bit a bit entre plataformas, versões ou dispositivos. Mesmo render repetível não prova por si só equivalência anatômica com uma imagem 2D. Seed fixa não transforma geração livre em geometria fixa.

Estados de revisão: `BLOQUEADO — SEM ATIVO MESTRE`, `REPROVADO — DIVERGÊNCIA` ou `VALIDADO NO ESCOPO DOCUMENTADO`. A validação exige evidência e escopo explícitos; itens não verificáveis impedem uma alegação de preservação integral. Não gerar repetidamente tentando obter por acaso uma garantia que a ferramenta não oferece.

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
4. Se houver divergência visível, reprove a saída. No requisito de preservação integral, não usar novas tentativas de geração livre como substituto do ativo mestre. Edições exploratórias só se aplicam quando o usuário autorizar explicitamente estudos com variação; nunca validam identidade integral.
5. Não prometa equivalência exata de pixels em uma pose nova gerada. Preserve o design verificável e sinalize detalhes pequenos que não possam ser conferidos na resolução disponível.

## Arquivos e entrega

Salve versões distintas em `assets/concept-art/<personagem>/`, sem sobrescrever a mestra nem a candidata anterior. Use nomes como `<personagem>_estudo_movimento_v02_candidata.png`. Salve um relatório Markdown associado com fontes, intenção, matriz antes/depois, divergências e operações realizadas. Registre a candidata no inventário sem alterar designações oficiais. Não aplique logotipo gerado; siga a skill de direção de arte se a marca for necessária.

Status inicial: **CANDIDATA — NÃO APROVADA**. O pedido de gerar, salvar ou fazer push não aprova a imagem como referência oficial. Informe os caminhos e forneça acesso verificável ao arquivo; não repita links internos como se fossem downloads públicos. Push somente quando autorizado na conversa.
