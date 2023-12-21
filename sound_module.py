#音声出力
import pygame

#時間計測
import time

#居眠り検知を知らせる関数
def sound():

    #soundfile変数に音声ファイルを格納
    soundfile = "Warning-Siren01-1.mp3"

    #初期化
    pygame.mixer.init()

    #音声ファイル読み込み
    pygame.mixer.music.load(soundfile)

    #再生開始
    pygame.mixer.music.play(1)
    
    #再生後1秒待つ
    time.sleep(1)

    #音声停止
    pygame.mixer.music.stop()

