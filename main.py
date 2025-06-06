import cv2
import mediapipe as mp
import time

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

LIMIAR_IMOBILIDADE = 7
AUSENCIA_LIMITE = 7 
DURACAO_ALERTA_AUSENCIA = 5
TOLERANCIA_MOVIMENTO = 10

tempo_inicial = None
tempo_parado = 0
tempo_ausente = None
tempo_alerta = None
desmaio_detectado = False
alerta_emitido = False

ultimo_ponto_nariz = None
ultimo_ponto_ombro = None

def houve_movimento(atual, ultimo, tolerancia=TOLERANCIA_MOVIMENTO):
    if atual is None or ultimo is None:
        return True
    dx = abs(atual.x - ultimo.x)
    dy = abs(atual.y - ultimo.y)
    return dx > tolerancia / 100 or dy > tolerancia / 100

cap = cv2.VideoCapture(0)

while cap.isOpened():
    sucesso, frame = cap.read()
    if not sucesso:
        print("Erro ao acessar a câmera.")
        break

    imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = pose.process(imagem_rgb)

    if resultados.pose_landmarks:
        mp_drawing.draw_landmarks(frame, resultados.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        landmarks = resultados.pose_landmarks.landmark
        nariz = landmarks[mp_pose.PoseLandmark.NOSE]
        pescoco = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        quadril = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
        mao_esq = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
        mao_dir = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
        olho_esq = landmarks[mp_pose.PoseLandmark.LEFT_EYE]
        olho_dir = landmarks[mp_pose.PoseLandmark.RIGHT_EYE]

        # Fadiga por cabeça baixa
        if nariz.y > pescoco.y - 0.15:
            cv2.putText(frame, "Fadiga: cabeça levemente inclinada", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Fadiga com mão no rosto
        if abs(mao_esq.x - olho_esq.x) < 0.1 and abs(mao_esq.y - olho_esq.y) < 0.1:
            cv2.putText(frame, "Mão no rosto detectada (fadiga)", (30, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        elif abs(mao_dir.x - olho_dir.x) < 0.1 and abs(mao_dir.y - olho_dir.y) < 0.1:
            cv2.putText(frame, "Mão no rosto detectada (fadiga)", (30, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Fadiga por postura inclinada
        inclinacao_tronco = abs(pescoco.y - quadril.y)
        if inclinacao_tronco < 0.25:
            cv2.putText(frame, "Postura de fadiga detectada", (30, 110),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Desmaio por imobilidade
        if not houve_movimento(nariz, ultimo_ponto_nariz) and not houve_movimento(pescoco, ultimo_ponto_ombro):
            if tempo_inicial is None:
                tempo_inicial = time.time()
            else:
                tempo_parado = time.time() - tempo_inicial

            if tempo_parado >= LIMIAR_IMOBILIDADE and not desmaio_detectado:
                cv2.putText(frame, "POSSÍVEL DESMAIO! Ligando para emergência...", (30, 140),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
                desmaio_detectado = True
        else:
            tempo_inicial = None
            tempo_parado = 0
            desmaio_detectado = False

        # Desmaio por queda frontal/costas
        ys = [lm.y for lm in landmarks]
        altura_pose = max(ys) - min(ys)
        if altura_pose < 0.2:
            cv2.putText(frame, "Corpo possivelmente deitado (queda?)", (30, 170),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            if not desmaio_detectado:
                cv2.putText(frame, "DESMAIO DETECTADO! Ligando para emergência...", (30, 200),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
                desmaio_detectado = True

        # Desmaio por queda lateral
        ombro_esq = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        ombro_dir = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        quadril_esq = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
        quadril_dir = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]

        largura_ombros = abs(ombro_esq.x - ombro_dir.x)
        altura_ombros = abs(ombro_esq.y - ombro_dir.y)
        altura_quadris = abs(quadril_esq.y - quadril_dir.y)

        if largura_ombros > 0.3 and altura_ombros < 0.05 and altura_quadris < 0.05:
            cv2.putText(frame, "Corpo possivelmente tombado lateralmente", (30, 230),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            if not desmaio_detectado:
                cv2.putText(frame, "DESMAIO DETECTADO! Ligando para emergência...", (30, 260),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
                desmaio_detectado = True

        tempo_ausente = None
        tempo_alerta = None
        alerta_emitido = False
        ultimo_ponto_nariz = nariz
        ultimo_ponto_ombro = pescoco

    else:
        if tempo_ausente is None:
            tempo_ausente = time.time()
        else:
            tempo_fora = time.time() - tempo_ausente
            if tempo_fora >= AUSENCIA_LIMITE and not alerta_emitido:
                alerta_emitido = True
                tempo_alerta = time.time()

        if alerta_emitido and tempo_alerta is not None:
            if time.time() - tempo_alerta <= DURACAO_ALERTA_AUSENCIA:
                cv2.putText(frame, "NENHUM CORPO DETECTADO! Verifique a situação!", (30, 290),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                alerta_emitido = False
                tempo_ausente = None
                tempo_alerta = None

    cv2.imshow('Detector de Fadiga Térmica', frame)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()