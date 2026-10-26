# Augusto — cabeça, bloco de volumes v01

**PROPOSTA TÉCNICA — NÃO APROVADA. Não é o modelo mestre nem reproduz a identidade integral do retrato.**

## Entrega

- `augusto_cabeca_blockout_v01.blend`: volumes editáveis separados, três câmeras ortográficas e retrato aprovado empacotado como imagem de referência (sem aparecer nos renders).
- `frente.png`, `perfil.png`, `tres-quartos.png`: renderizações da mesma geometria fixa.
- `build.py`: construção reproduzível dos volumes e das câmeras no Blender 4.3.2.
- `manifest.json`: versão do Blender, hash da referência e hashes dos arquivos gerados. Não constitui aprovação nem prova de fidelidade anatômica.

O retrato aprovado em DEC-017 é a fonte visual. A modelagem é interpretação manual codificada em volumes, não reconstrução automática confiável a partir de uma imagem. Unidades arbitrárias; não estabelecem altura, idade, medidas cranianas ou corpo inteiro. Nenhum cânone foi alterado.

## Revisão inicial

| Grupo | Resultado |
|---|---|
| Cabelo | Massa provisória escura e temporais cinzas; mechas e silhueta divergentes, precisam de escultura |
| Olhos | Marcadores geométricos; formato/pálpebras não reproduzem o retrato. Cor não definida |
| Pele | Material neutro de estudo, não paleta aprovada |
| Rosto | Plano de mandíbula angular proposto; nariz em cunha, boca e orelhas simplificados. Identidade facial não atingida |
| Proporções | Relações de crânio, profundidade e pescoço estimadas, sem medidas aprovadas; perfil e costas desconhecidos no retrato |
| Figurino | Fora do escopo deste bloco de cabeça; sem terno ou corpo modelado |
| Paleta | Materiais técnicos de argila, sem substituir as cores da imagem-mestra |

Sem rig, blendshapes, topologia de animação, texturas finais ou validação de deformações. As peças separadas se intersectam; isso é geometria de construção, não malha final. Não aprovar este bloco como identidade nem expandir para poses finais antes de ajustar e revisar rosto e silhueta.

## Reprodução

Na raiz do repositório, com Blender 4.3.2:

```sh
blender -b -t 2 --python assets/3d/augusto/blockout-v01/build.py
```

O script verifica o SHA-256 da referência antes de executar; interrompe se ela for alterada. O arquivo `.blend` contém a referência empacotada. Reexecutar regenera os arquivos desta pasta; preservar revisões manuais em uma versão distinta antes disso. Hash binário de `.blend` pode mudar com metadados; repetibilidade visual deve ser verificada separadamente. Sem garantia entre plataformas ou versões.

## Próxima etapa

## Verificação executada

Blender 4.3.2 gerou o arquivo e as três vistas sem erros. O `.blend` foi reaberto em outro processo e a câmera em três quartos foi renderizada novamente. As matrizes RGBA das duas imagens são idênticas pixel a pixel; os bytes dos PNGs diferem, sem diferença nos pixels, portanto não se alega igualdade binária de arquivo. Os hashes dos quatro arquivos do manifesto foram conferidos. Esse resultado vale para a cena estática e ambiente usados, não prova identidade anatômica nem repetibilidade entre máquinas. A referência original foi verificada pelo hash antes da modelagem.

## Refinamento pendente

Esculpir proporções e planos faciais comparando ao retrato aprovado; ajustar olhos/pálpebras, nariz, boca, mandíbula, orelhas e silhueta do cabelo. Depois apresentar vistas de revisão com as lacunas de perfil/costas identificadas. A simples existência das três câmeras não aprova essas vistas.
