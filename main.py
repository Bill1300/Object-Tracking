import cv2
from tracker import *

# Cria o objeto restreador.
tracker = EuclideanDistTracker()

#Cria o objeto de leitura de frames do video.
cap = cv2.VideoCapture("highway.mp4")

#Cria o objeto de deteccao de camera estavel.
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)
    #history: Indica quantos quadros anteriores são usados para construir o modelo de fundo.
    #varThreshold: Limitador de deteccao.

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape

    # Extrai uma regiao de interesse.
    roi = frame[340: 720,500: 800]
    
    # 1. Deteccao de Objetos.

    #Cria a mascara de deteccao de objetos.
    mask = object_detector.apply(roi)
    #Remove as sombras da mascara.
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        # Calcula a area e remove pequenos elementos. 
        area = cv2.contourArea(cnt)
        if area > 100:
            #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2) #Desenha contorno em elementos.
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])

    # 2. Objeto rastreador.
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("roi", roi) #Cria tela de area de deteccao.
    cv2.imshow("Frame", frame) #Cria tela de area completa.
    cv2.imshow("Mask", mask) #Cria tela de mascara.
    
    #Define ESC para sair.
    key = cv2.waitKey(30)
    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()