from flask import Flask
import librosa
import numpy as np
import firebase_admin
import librosa.display
import matplotlib.pyplot as plt
from firebase_admin import storage
from firebase_admin import credentials
import matplotlib
matplotlib.use('Agg')　# バックエンドを指定

app = Flask(__name__)


def get_bucket():
    "Cloud Storage for Firebaseにアクセス"
    try:
        app = firebase_admin.get_app() #　Appインスタンスを取得
    except ValueError as e:
        # バケットの参照を取得
        cred = credentials.Certificate('oral-voice-14555-firebase-adminsdk-9d2a4-895b1df1a3.json')
        firebase_admin.initialize_app(cred, {'storageBucket': 'oral-voice-14555.appspot.com'})
    bucket = storage.bucket()
    return bucket


def download_blob(bucket, source_blob_name, destination_file_name):
    """"バケットからblobをダウンロード"""
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print('Blob {} downloaded to {}.'.format(source_blob_name,destination_file_name))


def upload_blob(bucket, source_file_name, destination_blob_name):
    """"ファイルをバケットにアップロード"""
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print('File {} uploaded to {}.'.format(source_file_name,destination_blob_name))

def create_melspectrogram():
    """"メルスペクトログラムを作成"""
    data, fs = librosa.load("user.wav", sr=None)
    S = librosa.feature.melspectrogram(data, sr=fs, n_mels=128)
    log_S = librosa.amplitude_to_db(S, ref=np.max)
    plt.figure(figsize=(2.56, 2.56))　# 画像サイズを256×256に設定
    librosa.display.specshow(log_S, sr=fs)
    plt.axis("off")　# 枠と目盛りを消去
    plt.savefig("user.png")
    plt.close()

@app.route('/')
def main():
    bucket = get_bucket()
    download_blob(bucket, "test.wav", "user.wav")
    create_melspectrogram()
    upload_blob(bucket, "user.png", "test.png")
    return "END"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
