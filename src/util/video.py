import os

import cv2


def video(videoName: str, saveDir: str) -> None:
    try:
        if not os.path.isfile(videoName):
            return
        if not os.path.isdir(saveDir):
            os.mkdir(os.path.abspath(saveDir))
        # 读取视频文件
        cap = cv2.VideoCapture(videoName)

        # 视频中总共的帧数
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # 提取每一帧
        for i in range(frame_count):
            # 读取一帧
            ret, frame = cap.read()
            if not ret:
                break

            # 保存为图像文件
            filename = f"{saveDir}/frame_{i}.jpg"
            cv2.imencode(".jpg", frame)[1].tofile(filename)

        # 释放资源
        cap.release()
    except:
        pass
