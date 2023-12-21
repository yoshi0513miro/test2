#OpenCV
import cv2

#時間計測
import time

#居眠り通知音モジュール
import sound_module

#あくび通知音モジュール
import sound_module2

#----------------------------------------------------------------------------------------------------

#居眠りシステムの関数
def snooz_alery():
    
    #カメラを起動
    cap = cv2.VideoCapture(0)

    #居眠りの開始時間を指定
    start_time = time.time()

    #あくびの開始時間を指定
    start_time2 = time.time()

    #居眠り経過時間の初期化
    end_time = start_time

    #あくび経過時間の初期化
    end_time2 = start_time2
    
#----------------------------------------------------------------------------------------------------
    
    #無限ループ
    while True:
        
        #顔のカスケードファイルを用意
        cascade_file = "haarcascade_frontalface_default.xml"

        #顔のカスケードファイルを読み込み
        cascade = cv2.CascadeClassifier(cascade_file)

        #目のカスケードファイルを用意
        cascade_file2 = "haarcascade_eye_tree_eyeglasses.xml"
        
        #目のカスケードファイルを読み込み
        cascade2 = cv2.CascadeClassifier(cascade_file2)

        #口のカスケードファイルを用意
        cascade_file3 = "haarcascade_mcs_mouth.xml" 

        #口のカスケードファイルを読み込み
        cascade3 = cv2.CascadeClassifier(cascade_file3)

    #----------------------------------------------------------------------------------------------------
        
        #1フレームずつ取得
        ret, frame = cap.read()

        #左右反転
        frame = cv2.flip(frame, 1)

        #取得できなかったら
        if not ret:

            #終了
            break
        
        #画像を縮小
        frame = cv2.resize(frame, (500, 300))

        #グレイスケールに変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #----------------------------------------------------------------------------------------------------
        
        #顔の認識を実行
        face_list = cascade.detectMultiScale((gray), scaleFactor=1.1, minNeighbors=3, minSize=(100,100))

        #目の認識を実行
        eyes_list = cascade2.detectMultiScale((gray), scaleFactor=1.1, minNeighbors=3, minSize=(10,10),maxSize=(90,90))

        #口の認識を実行
        mouth_list = cascade3.detectMultiScale((gray), scaleFactor=1.1, minNeighbors=90, minSize=(10,10),maxSize=(90,90))

    #---------------------------------------------------------------------------------------------------- 
           
        #顔の部分を四角で囲む
        for (x,y,w,h) in face_list:

            #青色定義
            blue = (255,0,0)
            
            #青色の枠で囲む
            cv2.rectangle(frame, (x,y), (x+w,y+h),blue, 1)

        #目の部分を四角で囲む
        for (x,y,w,h) in eyes_list:

            #緑色定義
            green = (0,255,0)

            #緑色の枠で囲む
            cv2.rectangle(frame, (x,y), (x+w,y+h),green, 1)

        
        #口の部分を四角で囲む
        for (x,y,w,h) in mouth_list:

            #赤色定義
            red = (0,0,255)

            #赤色の枠で囲む
            cv2.rectangle(frame, (x,y), (x+w,y+h),red, 1)

    #----------------------------------------------------------------------------------------------------   
          
        #顔が検出できなかったら
        if len(face_list) == 0:
            
            #居眠り経過時間をもとに戻す
            start_time = end_time  

            #あくび経過時間をもとに戻す
            start_time2 = end_time2  

    #---------------------------------------------------------------------------------------------------- 

        #目が検出できなかったら
        if len(eyes_list) == 0:
                
            #経過時間を指定する
            end_time = time.time()
            
            #始まりの時間から経過時間を表示する
            print(end_time-start_time)

            #4秒経過したら
            if end_time-start_time >= 4:
                    
                #音源を再生
                sound_module.sound()
                
                #「INEMURI」と表示
                cv2.putText(frame,"INEMURI",(10,70),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,255),2,cv2.LINE_AA)
                
        #目を検出したら
        else:
            
            #経過時間を指定する
            start_time = time.time()

        #---------------------------------------------------------------------------------------------------- 
                    
        #口が検出できなかったら
        if len(mouth_list) == 0:
            
            #口検知の経過時間を指定する
            end_time2 = time.time()

            #3秒経過したら
            if end_time2 - start_time2 >= 5:

                #音源を再生
                sound_module2.sound2()

                #「AKUBI」と表示
                cv2.putText(frame,"AKUBI",(10,100),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,255),2,cv2.LINE_AA)
            
        #口を検出したら
        else:

            #経過時間を指定する 
            start_time2 = time.time() 

    #---------------------------------------------------------------------------------------------------- 

        #フレーム名  
        cv2.imshow("inemuri", frame)

        
        #キーボードが押されるまで処理を待つ
        key = cv2.waitKey(1)

        #エンターが押されたら
        if key == 13:
            
            #終了
            break

    #----------------------------------------------------------------------------------------------------       
        
    #カメラを閉じる
    cap.release()

    #ウィンドウを閉じる
    cv2.destroyAllWindows()