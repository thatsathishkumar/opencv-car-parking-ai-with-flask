import cv2
import pickle

height, width = 107, 48

try:
    with open("parkingSlotPosition", "rb") as f:
        posList = pickle.load(f)

except:
    posList = []

def mousClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open("parkingSlotPositon", "wb") as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread("carParkImg.png")
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 255, 255), 2)
    
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mousClick)
    cv2.waitKey(1)