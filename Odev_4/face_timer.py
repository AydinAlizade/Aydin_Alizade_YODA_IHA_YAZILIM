import cv2 as cv
import time
from collections import deque

# --- Sabitler ---
HAAR_CASCADE_PATH = 'Odev_4/Essentials/haar_face.xml'
VIDEO_SOURCE = 0

MAX_POINTS = 60
MISS_THRESHOLD = 10  # Tracker'ın kaybetmesine tolerans verilen max frame

# Veri yapıları
center_points = deque(maxlen=MAX_POINTS) # Yüz merkez noktalarını saklar

detection_start_time = None # Yüz tespit edildiğinde zaman damgası
detection_counter = 0  # Yüz tespit süresi

tracker = None
tracking = False
missed_frames = 0

# Haar Cascade yükle
haar = cv.CascadeClassifier(HAAR_CASCADE_PATH)

# Kamera aç
cap = cv.VideoCapture(VIDEO_SOURCE)
if not cap.isOpened():
    print("Kamera açılamadı.")
    exit()


def draw_tracking_line(frame, points):
    for i in range(1, len(points)):
        if points[i-1] and points[i]:
            cv.line(frame, points[i-1], points[i], (255, 0, 255), 2)


# ------------------ ANA LOOP ------------------
while True:
    ret, frame = cap.read() # boolean ve frame döner
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    face_detected = False
    face_box = None

    # --- 1) Eğer takip yoksa yüz tespiti yapılır ---
    if not tracking:
        faces = haar.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            face_box = (x, y, w, h)
            face_detected = True

            # Tracker başlat
            tracker = cv.TrackerKCF_create() # Boş bir tracker objesi oluşturur
            tracker.init(frame, tuple(face_box)) # Tracker'ı ilk yüz konumuyla başlatır
            tracking = True

            # Sayaç başlat
            detection_start_time = time.time()

    else:
        # --- 2) Takip aktifse tracker üzerinden yüzü güncelle ---
        ok, box = tracker.update(frame) # Haar cascade her frame'de yüz ararsa yavaş olur. Tracker bir kez tespit eilen yüzü takip eder.

        if ok:
            (x, y, w, h) = [int(v) for v in box]
            face_box = (x, y, w, h)
            face_detected = True
            missed_frames = 0
        else:
            missed_frames += 1

            if missed_frames >= MISS_THRESHOLD:
                # Gerçekten yüz kayboldu
                tracking = False
                tracker = None
                missed_frames = 0

                detection_start_time = None
                detection_counter = 0
                center_points.clear()

            face_detected = False

    # --- 3) Yüz varsa çizimler ve sayaç ---
    if face_detected and face_box is not None:
        (x, y, w, h) = face_box

        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        center = (x + w // 2, y + h // 2)
        center_points.append(center)

        cv.circle(frame, center, 5, (0, 0, 255), -1)

        # Merkez sol üstte
        cv.putText(frame, f"Merkez: {center}", (10, 30),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Merkez koordinatları yüzün üstünde
        # FONT = cv.FONT_HERSHEY_SIMPLEX
        # TEXT_COLOR = (255, 255, 255)
        # text_coords = f'Merkez: ({center[0]}, {center[1]})'
        # cv.putText(frame, text_coords, (max(5, center[0]-80), max(20, center[1]-10)), FONT, 0.6, TEXT_COLOR, 1)

        # Süre hesapla
        if detection_start_time:
            detection_counter = int(time.time() - detection_start_time)

    # --- 4) Hareket çizgisi ---
    draw_tracking_line(frame, center_points)

    # --- 5) Süre sağ üstte ---
    cv.putText(frame, f"{detection_counter} saniye",
               (frame.shape[1] - 120, 30),
               cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # --- 6) Göster ---
    cv.imshow("Yuz Takip", frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()