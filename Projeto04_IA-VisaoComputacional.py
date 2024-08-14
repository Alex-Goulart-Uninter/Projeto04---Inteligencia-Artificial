#Código do projeto
import cv2
from cvzone.HandTrackingModule import HandDetector

# Inicializa a webcam
webcan = cv2.VideoCapture(0)

# Inicializa o rastreador de mãos
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
# Captura a imagem da webcam
    sucesso, imagem = webcan.read()
    
# Detecta as mãos no quadro
    hands,imagem_maos=rastreador.findHands(imagem)
    
# Mostra o quadro com as marcações
    cv2.imshow("Projeto04 IA", imagem_maos)

# Encerra a aplicação quando qualquer tecla é pressionada
    if cv2.waitKey(1) != -1:
        break

# Libera a câmera e fecha as janelas
webcan.release()
cv2.destroyAllWindows()