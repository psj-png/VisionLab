import cv2 as cv
import numpy as np

url = "rtsp://210.99.70.120:1935/live/cctv001.stream"
cap = cv.VideoCapture(url)

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fps = 20.0

fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = None
is_recording = False

brightness = 0
zoom_factor = 1.0
move_x, move_y = 0, 0

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret: break

    if brightness != 0:
        matrix = np.full(frame.shape, abs(brightness), dtype=np.uint8)
        if brightness > 0:
            frame = cv.add(frame, matrix)
        else:
            frame = cv.subtract(frame, matrix)

    if zoom_factor > 1.0:
        new_w, new_h = int(width / zoom_factor), int(height / zoom_factor)
        cx, cy = width // 2 + move_x, height // 2 + move_y

        x1 = max(0, min(cx - new_w // 2, width - new_w))
        y1 = max(0, min(cy - new_h // 2, height - new_h))

        frame = frame[y1:y1 + new_h, x1:x1 + new_w]
        frame = cv.resize(frame, (width, height))
    else:
        move_x, move_y = 0, 0
        zoom_factor = 1.0

    record_frame = frame.copy()
    display_img = frame.copy()

    if is_recording:
        text = "REC"
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        thickness = 2
        text_size = cv.getTextSize(text, font, font_scale, thickness)[0]

        center_x = width // 2
        text_x = center_x - (text_size[0] // 2) + 15

        cv.circle(display_img, (text_x - 25, 40), 10, (0, 0, 255), -1)
        cv.putText(display_img, text, (text_x, 53), font, font_scale, (0, 0, 255), thickness)

        if out is not None:
            out.write(record_frame)

    status = f"B: {brightness} | Zoom: {zoom_factor:.1f}x"
    cv.putText(display_img, status, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    cv.imshow('Vision System - Traffic Monitor', display_img)

    key = cv.waitKey(1) & 0xFF

    if key == 27:
        break
    elif key == ord(' '):
        is_recording = not is_recording
        if is_recording:
            out = cv.VideoWriter('output.avi', fourcc, fps, (width, height))
            if out.isOpened():
                print("Recording started...")
        else:
            if out is not None:
                out.release()
                print("Recording stopped and saved as output.avi.")


    elif key == ord('z'):
        zoom_factor = min(zoom_factor + 0.5, 5.0)
    elif key == ord('x'):
        zoom_factor = max(zoom_factor - 0.5, 1.0)


    elif key == ord('w'):
        move_y -= 30
    elif key == ord('s'):
        move_y += 30
    elif key == ord('a'):
        move_x -= 30
    elif key == ord('d'):
        move_x += 30

    elif key == ord('b'):
        brightness = min(brightness + 10, 100)
    elif key == ord('n'):
        brightness = max(brightness - 10, -100)


cap.release()
if out is not None:
    out.release()
cv.destroyAllWindows()
