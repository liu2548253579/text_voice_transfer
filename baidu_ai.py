from aip import AipSpeech

APP_ID=None
API_KEY=None
SECRET_KEY=None

#从baidu_api.txt中读取APP_ID, API_KEY, SECRET_KEY,格式为APP_ID:xxxxx 以此类推
with open('baidu_api.txt', 'r') as f:
    lines = f.readlines()
    APP_ID = lines[0].split(':')[1].strip()
    API_KEY = lines[1].split(':')[1].strip()
    SECRET_KEY = lines[2].split(':')[1].strip()

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def audio_to_text(wav_file):
    #读取音频文件
    with open(wav_file, 'rb') as fp:
        file_context = fp.read()
    # 识别本地文件
    res = client.asr(file_context, 'wav', 16000, {'dev_pid': 1537})     #res为字典类型
    res_str = res['result'][0]
    return res_str

def text_to_audio(synth_file, res_str):
    # 准备语音合成
    synth_context = client.synthesis(res_str,'zh',1,{
        'spd' : 5,  #语速(0-9)
        'vol' : 5,  #音量(0-9)
        'pit' : 5,  #音调(0-9)
        'per' : 4,  #发音人·0：女声，1：男声，3：情感合成-度逍遥，4：情感合成-度丫丫
    })

    # 确定合成内容已生成，因为生成错误会返回字典类型报错
    if not isinstance(synth_context, dict):
        with open(synth_file, 'wb') as f:
            f.write(synth_context)
        return 0
    else:
        return -1