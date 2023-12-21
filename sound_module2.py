#音声出力
import pygame

#時間計測
import time

#あくび検知を知らせる関数
def sound2():

    #soundfile2変数に音声ファイルを格納
    soundfile2 = "enter30.mp3"

    #初期化
    pygame.mixer.init()

    #音声ファイル読み込み
    pygame.mixer.music.load(soundfile2)

    #再生開始
    pygame.mixer.music.play(1)

    #再生後0.5秒待つ
    time.sleep(0.5)

    #音声停止
    pygame.mixer.music.stop()