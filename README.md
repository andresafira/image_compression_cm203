# Image Compression

## Módulo fft


Nesse módulo estão as implementações base das funções a serem utilizadas, bem como funções auxiliares para facilitar a implementação e legibilidade do código. A seguir está contida uma descrição das principais funções implementadas no módulo FFT:


- [ ]  ```fft(x, inv=1)```: Função que realiza a transformada rápida de Fourier de um vetor unidimensional com tamanho correspondente a uma potência de dois, através do algoritmo recursivo.

- [ ] ```fft_inplace(x, inv=1)```: Função que realiza a transformada rápida de Fourier de um vetor unidimensional com tamanho correspondente a uma potência de dois, através do algoritmo que realiza as transformadas no próprio vetor, sem utilizar recursão, o que otimiza o alocamento de memória.

- [ ] ```fft2(img, tech)```: Função que realiza a transformada rápida de Fourier de um vetor bidimensional com tamanho correspondente a uma potência de dois, através do algoritmo escolhido por meio do seu parâmetro \texttt{tech}. Ela realiza a transformada primeiramente em suas linhas e posteriormente nas colunas do vetor.

- [ ] ```ifft(X)```: Função que realiza a transforma rápida inversa de Fourier de um vetor unidimensional com tamanho correspondente a uma potência de dois, através do algoritmo recursivo. Ele utiliza a implementação da ```fft()} utilizando o parâmetro $inv = -1$ e dividindo pelo tamanho do vetor no final.

- [ ] ```ifft_inplace(X)```: Função que realiza a transforma rápida inversa de Fourier de um vetor unidimensional com tamanho correspondente a uma potência de dois, através do algoritmo que realiza as transformadas no próprio vetor, sem utilizar recursão, o que otimiza o alocamento de memória. Ele utiliza a implementação da ```fft\_inplace()} utilizando o parâmetro $inv = -1$ e dividindo pelo tamanho do vetor no final.

- [ ] ```ifft2(img, tech)```: Função que realiza a transformada rápida inversa de Fourier de um vetor bidimensional com tamanho correspondente a uma potência de dois, através do algoritmo escolhido por meio do seu parâmetro \texttt{tech}. A fim de inverter o efeito de ```fft2()} essa função realiza as transformadas inversas primeiro em relação às colunas e posteriomente em relação às linhas, divindo pelo tamanho do vetor no final.



## Módulo image

Esse módulo é responsável por processar as imagens a fim de adequá-las para o estado de entrada nas técnicas de compressão, ajustar o estado de saída (removendo números complexos e ajustando o tipo de imagem), bem como realizar a operação de compressão e ajuste de canais de cores. As funções utilizadas serão listadas a seguir:

- [ ] ```type_adjustment(img)```: Realiza o ajuste da imagem de saída, a fim de limitar os valores no intervalo de cores de pixel suportados: $[0, 255]$, bem como ajustar o tipo de saída para $np.uint8$ que é um tipo aceito pela biblioteca de imagens $PIL$.

- [ ] ```expand(img)```: Expande as dimensões da imagem para as potências de dois mais próximas, a fim de usar as técnicas desenvolvidas. Os valores adicionados são 0 por padrão.

- [ ] ```contract(img, original_shape)```: Contrai a imagem, desfazendo a operação da função anterior.

- [ ] ```compress(img, compression_factor, tech)```: Realiza a compressão da imagem com possivelmente mais de um canal de cor, segundo a técnica explicitada na Introdução deste trabalho utilizando o algoritmo especificado pelo parâmetro $tech$, que pode ser $recursive$ ou $inplace$.

- [ ] ```compress_monotone(img, compression_factor, tech)```: Realiza a compressão da imagem com exclusivamente um canal de cor (a imagem deve portanto ser unidimensional), segundo a técnica explicitada na Introdução deste trabalho utilizando o algoritmo especificado pelo parâmetro $tech$, que pode ser $recursive$ ou $inplace$.


## Módulo utils

Esse módulo adicional contém a implementação de algumas funções não necessariamente relacionadas utilizadas em outros módulos a fim de facilitar a aplicação e legibilidade do código. As funções implementadas são:

- [ ] ```get_inv_binary_associate(i, size)```: Calcula o número cuja representação binária ao contrário é igual à representação binária do parâmetro $i$. Essa função é utilizada para realizar a operação de inversão bit-a-bit utilizada no algoritmo $inplace$. O parâmetro $size$ é necessário pois algumas representações inversas podem ser diferentes, dependendo de quantos bits se tem para a alocação de um número, exemplo: $(0001)_2^{-1} = (1000)_2 \neq (1)_2 = (1)_2^{-1}$ por mais que $(0001)_2 = (1)_2$.

- [ ] ```swap(arr, index1, index2)```: Troca o conteúdo dos índices $index1$ e $index2$ do vetor $arr$.

- [ ] ```bitwise_invert(arr, n, log\_n)```: Realiza a operação de inversão bit-a-bit do vetor $arr$. Isso ocorre quando leva-se o conteúdo da posição $i$ para a posição cuja representação binária é o contrário da representação binária de $i$.
