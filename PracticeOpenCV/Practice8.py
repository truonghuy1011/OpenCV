   import cv2
   import sys
   my_track_method = cv2.TrackerMOSSE_create()
     cap = cv2.VideoCapture("race.mp4")
      ret , frame = cap.read()
      if not ret:
              print('Khong tim thay file video')   
               sys.exit()
               select_box = cv2.selectROI(frame, showCrosshair=True)
               my_track_method.init(frame, select_box)
               while True: 
                
                ok, frame = cap.read()
                   if not ok:       
                       
                           break   
                 ret, select_box = my_track_method.update(frame)   
             if ret:     
                tl, br  = (int(select_box[0]), int(select_box[1])), (int(select_box[0] + select_box[2]), 
                int(select_box[1] + select_box[3]))      
                  cv2.rectangle(frame, tl, br, (0, 255, 0), 2, 2)   
             else:      
                 cv2.putText(frame, "Object can not be tracked!", (80, 100), 
                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)   
                  cv2.putText(frame, "MiAI Demo Object Tracking", (80, 50),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2);    
                   cv2.imshow("Video", frame)  
                     key = cv2.waitKey(1) & 0xff<br><br>    
                        if key == ord('q'):     
                              break
                        if key == ord('s'):        
                          select_box = cv2.selectROI(frame, showCrosshair=True)
                        my_track_method.clear()       
                        my_track_method = cv2.TrackerMOSSE_create()
                        my_track_method.init(frame, select_box)