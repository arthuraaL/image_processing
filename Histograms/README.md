# Histograms
 
Histogramas sao graficos que apresentam uma distruicao de frequencia, e em imagens podemos definir um histograma como um grafico que descreve
quantos pixels existem com aquela intensidade (profundidade/luminosidade) especifica. Uma tipica imagem em tons de cinza de 8 bits possui valores de intensidade
variando de 0 a 255. Sendo 0 um pixel escuro e 255 um pixel claro (branco).

Um histograma pode ser definido pela funcao h(i) = numero de pixels com intensidade i.

Histogramas nao informam a localizacao do pixel, nem o seu arranjamento espacial. Mas pode-se usar um histograma para determinar a imagem original (fazer o procedimento inverso) ?

## Interpretando histogramas

Um histograma nos informa de problemas que podem ocorrer durante a aquisicao da imagem, como:
* Alto contraste 
* Possivel analisar a exposicao da luz em uma imagem