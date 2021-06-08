<img src="https://lh3.googleusercontent.com/proxy/l3sMUjTIJptTu0x_2MJBixbR447FptNuPU3FL-7_FMUKd-8MkKyVOF8mffpw7NpqFK4EK7Y7z9ICtJkFiKAzFR7_JVc81e4Uo9sqeB_cd0rUXGfl8IEwXjGUEhM_4bCgAyUUQ-A" height="64">
<p>
OpenCV (Open source Computer Vision) é uma biblioteca muito poderosa para tarefas de processamento de imagens
e aprendizado de máquina. A biblioteca é multiplataforma e você pode instalá-la pip (onde você a estiver usando com Python) com suporte de CPU.
Alternativamente, onde por exemplo você deseja usá-lo com suporte a GPU, você pode construí-lo a partir do código-fonte,
que é mais complexo.

O pacote instalado foi **opencv-contrib-python**, não é um pacote oficial da equipe [OpenCV](openCV.org), mas é mensionado na documentação e apresentado alguns tutorias. Esse diretório contém dois módulos principais junto com todas as funcionalidades do OpenCV padrão.
Ele foi instalado pois havia bibliotecas necessárias para o monitorando de movimentação de objetos na imagem. Este é seu comando para instalação:
</p>

>sudo apt update

>sudo apt install python3-pip

>sudo pip install opencv-contrib-python

---
### Introdução
O objetivo to projeto é monitorar os veículos passando em baixo de um viaduto em um vídeo e contá-los, com isso foi utilizado uma função de verificação de objeto de câmera estável chamada: **cv2.createBackgroundSubtractorMOG2**.

No script, a cada frame do vídeo capturado é verificado se há um novo objeto, e nesse loop é usada uma técnica de máscara, onde o toda a tela é definida na cor preta e as bordas de objetos com tamanho acima de 100 pixels são de cor branca, assim facilitando o reconhecimento (isso é apresentado na janela "mask"). Também é extraída do vídeo uma região de interesse, onde é localizada uma rodovia, com isso diminuindo bastante o número de erro nas contagens (isso é apresentado na janela "roi").

Após a identificar os veículos a função **tracker.update()** é utilizada, ela define a contagem do objeto em movimento, se mudando de local na tela. Com isso é criada um retangulo em volta do veículo e é salvo em um vetor (temporário) o local do objeto no eixo x e y, no pixel do vídeo e também um ID para ele.

Assim que o vídeo acaba as janelas nas fechadas e os valores apresentados no terminal não são salvos.

