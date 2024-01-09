import cv2
import numpy as np
from object_detection import ObjectDetection
import math

classes=["Person","Bird","Animal","Building","Tree"]
font = cv2.FONT_HERSHEY_PLAIN
color = (57, 255, 20)

od = ObjectDetection()

cap=cv2.VideoCapture(0)

count = 0
center_points_prev_frame = []

tracking_objects = {}
track_id = 0

while True:
    ret, frame = cap.read()
    count += 1
    if not ret:
        break

    center_points_cur_frame = []


    (class_ids, scores, boxes) = od.detect(frame)
    # print(class_ids,scores,boxes)
    for i, box in enumerate(boxes):
        (x, y, w, h) = box
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        center_points_cur_frame.append((cx, cy))

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(frame, classes[class_ids[i]], (x+10,y+20), font, 1, (255-color[0],255-color[1],255-color[2]), 2)

        

    if count <= 2:
        for pt in center_points_cur_frame:
            for pt2 in center_points_prev_frame:
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                if distance < 20:
                    tracking_objects[track_id] = pt
                    track_id += 1
    else:

        tracking_objects_copy = tracking_objects.copy()
        center_points_cur_frame_copy = center_points_cur_frame.copy()

        for object_id, pt2 in tracking_objects_copy.items():
            object_exists = False
            for pt in center_points_cur_frame_copy:
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                # Update IDs position
                if distance < 20:
                    tracking_objects[object_id] = pt
                    object_exists = True
                    if pt in center_points_cur_frame:
                        center_points_cur_frame.remove(pt)
                    continue

            # Remove IDs lost
            if not object_exists:
                tracking_objects.pop(object_id)

        # Add new IDs found
        for pt in center_points_cur_frame:
            tracking_objects[track_id] = pt
            track_id += 1


    cv2.imshow("Frame", frame)

    center_points_prev_frame = center_points_cur_frame.copy()

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
