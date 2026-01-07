import cv2

# 1️⃣ Load Haar Cascade (OpenCV default path se)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 2️⃣ Open Webcam
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("❌ Webcam open nahi ho rahi")
    exit()

print("✅ Webcam started... Press ESC to exit")

while True:
    # 3️⃣ Read frame
    ret, img = webcam.read()
    if not ret:
        print("❌ Frame read nahi ho paya")
        break

    # 4️⃣ Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 5️⃣ Face detection (improved parameters)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(40, 40)
    )

    # 6️⃣ Draw rectangle & count faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 7️⃣ Show face count text
    cv2.putText(
        img,
        f"Faces: {len(faces)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # 8️⃣ Display window
    cv2.imshow("Face Detection", img)

    # 9️⃣ Exit on ESC
    if cv2.waitKey(10) & 0xFF == 27:
        break

# 🔟 Release resources
webcam.release()
cv2.destroyAllWindows()
