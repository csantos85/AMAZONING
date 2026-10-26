---
name: amazoning-art-direction
description: Use quando preparar descrições visuais, criar pranchas, preservar personagens ou aplicar a identidade visual oficial de AMAZONING.
---

# Preservação visual e direção de arte

## Requisito de identidade integral entre versões

O criador exige que versões não apresentem diferenças físicas. Para poses e construção, aplique a seção **Preservação integral obrigatória** de `../amazoning-motion-studies/SKILL.md`: preservar pixels originais em estudos da mesma pose; para novas poses, usar ativo articulável mestre aprovado e controle de versões. Geração livre não oferece essa garantia. Saídas divergentes ou com identidade não verificável não atendem ao requisito, mesmo com status de candidata. Não declarar fidelidade integral por inspeção aproximada. Esta regra prevalece sobre os procedimentos de geração exploratória deste documento.

Todos os caminhos são relativos à raiz do repositório AMAZONING. Leia `AGENTS.md` e respeite sua ordem de autoridade. Esta Skill define o processo; não altera características canônicas.

## Identidade visual oficial

Antes de criar artbooks, documentos, apresentações ou materiais promocionais, consulte `assets/branding/README.md` e abra `assets/branding/amazoning_logo_oficial.png`, a referência principal e oficial do logotipo.

Aplique o arquivo original em composição, preservando tipografia, proporções, formas das letras e detalhe vermelho do símbolo A. Redimensione somente de modo proporcional. Não redesenhe, regenere, substitua a fonte, deforme, recorte partes ou recolora o logotipo. Logos em artes conceituais e imagens geradas não são substitutos oficiais.

Se o arquivo estiver ausente ou inacessível, registre a limitação e solicite o original; continue o planejamento, mas não improvise nem afirme ter aplicado ou validado o logotipo. A pendência do logo impede sua aplicação, não a análise documental ou a criação independente de personagens quando os requisitos próprios estiverem atendidos.

Antes de entregar, compare o logo aplicado com o original e registre o resultado da conferência. Não invente fonte, hexadecimais, margens ou variantes como especificações aprovadas. Novas versões requerem aprovação explícita e histórico, sem sobrescrever o original.

## Requisitos por personagem

Cada personagem deve possuir ficha canônica, imagem-mestra explicitamente aprovada pelo criador e histórico de versões. Consulte `assets/concept-art/master-inventory.md` para caminhos, disponibilidade, escopo da aprovação e substituições; consulte também `assets/concept-art/README.md` e `docs/decisions/decision-log.md`.

Não escolha uma imagem-mestra por conta própria. Nome de arquivo, data, qualidade, semelhança, geração bem-sucedida ou aprovação de outra imagem não constituem aprovação. Não promova automaticamente imagens geradas, edições ou composições a referências oficiais.

## Antes de qualquer criação visual

1. Identifique personagem, variante (civil, traje ou transformação), objetivo e referências aprovadas para esse escopo.
2. Leia a ficha correspondente: `docs/characters/lucas-mazweng.md` para Lucas e `docs/characters/jeff-a-brasa.md` para Jeff. Para outros personagens, use o caminho registrado no inventário, sem presumir ficha ou aprovação existente.
3. Abra e examine a imagem-mestra; citar seu caminho não basta. Se o arquivo estiver ausente, inacessível ou não aprovado, registre o impedimento e solicite a referência ou designação que falta. Continue a análise documental e o briefing; não gere nem redesenhe o personagem enquanto faltar esse requisito.
4. Compare imagem e ficha antes de gerar. Sinalize divergências ao criador; não resolva conflitos alterando cânone ou adotando detalhes da imagem silenciosamente.
5. Prepare uma matriz dos atributos abaixo com valor, fonte, classificação e eventuais divergências. Só prossiga com referências disponíveis e conflitos relevantes resolvidos.

## Classificação dos atributos

- **CONFIRMADA:** explicitamente sustentada pela ficha, decisão do criador ou imagem aprovada dentro do escopo documentado, respeitando a hierarquia de `AGENTS.md`.
- **ESTIMADA:** leitura aproximada, como proporção visual ou cor sob iluminação. Registre método e incerteza; não apresente como medida oficial nem a grave no cânone.
- **PENDENTE:** ausente, ambígua, conflitante ou sem aprovação. Não preencha como fato; solicite decisão quando necessária à criação.

A aprovação de uma imagem não confirma automaticamente medidas, hexadecimais, vistas não mostradas, variantes ou detalhes não documentados.

## Validação obrigatória antes e depois da criação

| Grupo | Conferência |
|---|---|
| Cabelo | Cor, corte, volume, textura, franja e silhueta. |
| Olhos | Cor, formato e distinção entre aparência normal e efeitos de transformação. |
| Pele | Tom documentado, considerando iluminação; não fixar hexadecimal por amostragem automática. |
| Estrutura facial | Maxilar, sobrancelhas e demais relações faciais visíveis; não inventar medidas. |
| Proporções | Porte, altura quando documentada e relações corporais; perspectiva não define altura oficial. |
| Figurino | Silhueta, peças, máscara, símbolos, acessórios e variante aprovada. |
| Paleta | Cores e códigos aprovados, distribuição e efeitos; não converter estimativas em códigos oficiais. |

Para Lucas: preservar cabelo preto e identidade vermelho/preto. Para Jeff: preservar cabelo loiro, olhos castanho-escuros, pele oliva, identidade azul/preto e Blue Fire. Os olhos brilhantes de Blue Fire são efeito descrito na ficha, não alteração permanente da cor dos olhos. Não reutilizar cabelo preto das pranchas superadas de Jeff.

Compare cada resultado com a imagem-mestra e a ficha usando a matriz completa. Marque cada item como conforme, divergente ou não verificável; item não verificável não equivale a aprovação. Preserve a identidade ao corrigir divergências e não copie personagens de terceiros.

## Pranchas coletivas

Priorize composição das imagens individuais aprovadas, sem redesenhar os personagens. Preserve rosto, proporções, figurino e paleta. Registre fontes e operações de montagem; não use deformação, recoloração ou preenchimento generativo para mudar a identidade. Escala de layout não determina alturas relativas canônicas. Se faltarem pose, recorte ou resolução adequados, sinalize a limitação antes de propor uma nova arte individual pelo mesmo processo de validação e aprovação.

Uma montagem não aprova automaticamente os componentes nem se torna imagem-mestra. Fundos e efeitos não devem ocultar divergências ou alterar características confirmadas.

## Aprovação e histórico de versões

1. Salve cada geração/edição como versão candidata distinta, sem sobrescrever ou excluir referências existentes. Status inicial: **CANDIDATA — NÃO APROVADA**.
2. Entregue a comparação e obtenha aprovação explícita do criador antes de designar ou substituir qualquer referência oficial. Pedido de geração não é aprovação do resultado.
3. Registre no inventário: personagem, variante, caminho, versão/identificador, status, disponibilidade, fonte e data da aprovação quando conhecidas, escopo, versão substituída e motivo. Use “não informada” para datas desconhecidas.
4. Só após aprovação, atualize a designação e registre a substituição; preserve o arquivo anterior como histórico SUPERADO. Não renomeie um arquivo para simular uma nova aprovação.
5. Alterações nas fichas ou decisões exigem autorização própria conforme `AGENTS.md`; não são consequência automática da validação visual.

## Entrega

Relate referências efetivamente consultadas, disponibilidade e, quando houver aplicação da marca, a conferência do logotipo oficial. Para personagens, inclua a matriz dos sete grupos, atributos confirmados/estimados/pendentes, divergências, operações de composição, status do resultado e decisões requeridas. Apresente o diff de qualquer atualização documental para revisão. Nunca declare uma imagem aprovada sem fonte explícita.
