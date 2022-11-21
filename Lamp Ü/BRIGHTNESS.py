import cv2
from PIL import Image, ImageStat

stream = cv2.VideoCapture(0)    # pake default camera
running = True
while running:                  # selama belum capture image
    capture, frame = stream.read()          # frame per frame di tunjukkin (jadi kyk streaming atau video)
    cv2.putText(frame, str(frame.shape[:2]), (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 4)  # nunjukkin size window
    frame = cv2.rectangle(frame, (60, 60), (580, 420), (255, 255, 0), 1)        # ngegambar kotak area fokus kontrol terang
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                             # convert ke grayscale (bewarna ke hitam putih)
    cv2.imshow('currently streaming!', frame)                                   # menunjukkan gambar
    if cv2.waitKey(1) & 0xFF == ord('q'):                                       # take a picture
        frame = frame[60:420, 60:580]                                           # crop sesuai luas kotak
        cv2.imwrite("Current_Image.bmp", frame)                                 # di save
        stream.release()                                                        # berhenti streaming
        cv2.destroyAllWindows()
        running = False
showing = Image.open("Current_Image.bmp").convert('L')
rmsValue = ImageStat.Stat(showing)                      # itung average brightness secara RMS
showWithStat = cv2.imread("Current_Image.bmp", 1)
cv2.putText(showWithStat, str(rmsValue.rms[0]), (240, 240), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 4)
cv2.imshow("now", showWithStat)
cv2.waitKey(0)
cv2.destroyAllWindows()