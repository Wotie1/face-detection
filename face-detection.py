
import cv2

# Yuz algilama modelini yukle
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

# Model kontrolu
if face_cascade.empty():
    print("HATA: Yuz algilama modeli yuklenemedi!")
    exit()

# Kamerayi baslat
cap = cv2.VideoCapture(0)

# Kamera kontrolu
if not cap.isOpened():
    print("HATA: Kamera acilamadi!")
    exit()

print("Face Detector baslatildi.")
print("Cikmak icin Q tusuna basin.")

try:
    while True:

        # Kameradan goruntu al
        ret, frame = cap.read()

        if not ret or frame is None:
            print("HATA: Kameradan goruntu alinamadi!")
            break

        # Goruntuyu gri tonlamaya cevir
        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # Yuzleri algila
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=4
        )

        # Algilanan yuzlerin etrafina dikdortgen ciz
        for (x, y, w, h) in faces:
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

        # Goruntuyu ekranda goster
        cv2.imshow("Face Detector", frame)

        # Q tusuyla cikis
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except cv2.error as e:
    print(f"OpenCV hatasi: {e}")

except Exception as e:
    print(f"Beklenmeyen hata: {e}")

finally:
    # Kaynaklari temizle
    cap.release()
    cv2.destroyAllWindows()

    print("Face Detector kapatildi.")
