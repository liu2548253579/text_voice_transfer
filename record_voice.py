import keyboard  
import pyaudio,wave
from tqdm import tqdm

def record(filename):
    p =  pyaudio.PyAudio()     
    FORMAT = pyaudio.paInt16   
    CHANNELS = 1                
    RATE = 16000              
    CHUNK = 1024  

    stream = p.open(rate=RATE,
                    format=FORMAT,
                    channels=CHANNELS,
                    input=True,              
                    frames_per_buffer=CHUNK)   

    frames = []

    print("按下空格键开始录制音频,按下s键停止录音。")
    recording = False 
    
    while True:
        
        try:       
            if keyboard.is_pressed(' '): 
                if not recording:
                    recording = True
                    print("开始录音...")       
            if keyboard.is_pressed('s') and recording: 
                    recording = False
                    print("录音结束。")
                    break     
        except:
            print('空格键检测失败,请手动停止录音。')     
        
        try:       
            data = stream.read(CHUNK)
            frames.append(data)
        except:
            pass  
            
        if not stream.is_active():
            print('录音意外停止!')
            break 

    stream.stop_stream()
    stream.close()      
    p.terminate()      

    wf = wave.open(filename, 'wb') 

    wf.setframerate(RATE)
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))   

    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":
    filename = input("wav文件保存名称(带后缀):")
    record(filename)
