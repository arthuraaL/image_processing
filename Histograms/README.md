# Histogramas
 
Histogramas sao graficos que apresentam uma distruicao de frequencia, e em imagens podemos definir um histograma como um grafico que descreve
quantos pixels existem com aquela intensidade (profundidade/luminosidade) especifica. Uma tipica imagem em tons de cinza de 8 bits possui valores de intensidade
variando de 0 a 255. Sendo 0 um pixel escuro e 255 um pixel claro (branco).

Um histograma pode ser definido pela funcao h(i) = numero de pixels com intensidade i.

Histogramas nao informam a localizacao do pixel, nem o seu arranjamento espacial. Mas pode-se usar um histograma para determinar a imagem original (fazer o procedimento inverso) ?

## Interpretando histogramas

Um histograma nos informa de problemas que podem ocorrer durante a aquisicao da imagem, como:
* Alto contraste 
* Possivel analisar a exposicao da luz em uma imagem

Point operations - podem ser usadas para alterar propriedades do histograma, como adicao, multiplicao, exp e log.

## Equalizacao de histogramas

Uma equalizacao tem por objetivo uniformizar uma distribuicao. Uma imagem equalizada eh mais bem distribuida do que a original.

Precisamos de uma funcao que transforme cada pixel original em um pixel diferente, a fim de obter um distribuicao uniforme.

- Obs:
    * A tecnica de equalizacao nao pode ser aplicada separadamente para cada canal da imagem, pois isso leva a uma mudanca drastica no balanco de cor da imagem.
    * 

Histogram equalization is good when histogram of the image is confined to a particular region. It won't work good in places where there is large intensity variations where histogram covers a large region, ie both bright and dark pixels are present. Please check the SOF links in Additional Resources.

## Adaptive Histogram Equalization


## Contrastive Limited Adaptive Equalization (clahe)




