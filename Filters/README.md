## FIltros

Os filtros servem, principalmente, para realizar alguma operacoes em uma imagem e gera uma saida que sera utilizada em outros processamentos.

* Kernel convolution
Eh o 'core' de filtros, como:
    1. Gaussian blur
    2. mean blur
    3. edge detection

kernel deve ter tamanhos impares -> (3x3), (5x5), ...

O kernel eh convoluido com a imagem a fim de gerar uma imagem de saida com uma informacao especifica.

Quando a janela eh multiplicada pelos pixels da imagem, somados e divididos pela quantidade de pixels do kernel. Ou seja, funciona como uma media ponderada, onde cada elemento da janela dara um 'peso' ou relevancia para aquele pixel da imagem em questao. 

Obs.: O resultado deve ser normalizado para que a imagem nao fique com um aspecto mais claro ou mais escuro.

#### Blur filter:
    * Remove ruido antes de algum processamento
    * Ou pode ser usado apenas para tornar imagens melhores

