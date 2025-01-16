from voice import VoiceAI
from threading import Thread
from queue import Queue
from json import loads
from translate_object import TranslateObject
import flet as ft   

queue = Queue()
queue_translator = Queue()

tr_ob = TranslateObject()

def start_ai_voice():
    ai = VoiceAI(vosk_name="vosk-model-en-us-0.42-gigaspeech")
    ai.voice(lambda obj: queue.put(obj))


def start_gui(page: ft.Page):
    
    page.title = "TOMZINHA SUBTITLE AI"

    t = ft.Text(value="", size=25)
    t2 = ft.Text(value="", size=25)
    
    page.window.height = 600
    page.window.width = 430
    
    cl = ft.Column(
        height=page.window.height - 70,
        col=6,
        scroll=ft.ScrollMode.ALWAYS,
        auto_scroll=True,
        adaptive=True,
        controls=[t]
    )

    cl_2 = ft.Column(
        height=page.window.height - 70,
        col=6,
        scroll=ft.ScrollMode.ALWAYS,
        auto_scroll=True,
        adaptive=True,
        controls=[t2]
    )
    
    tomzinha_name = ft.Text(value="contact: tomoliveira1995@gmail.com")

    row = ft.ResponsiveRow([
        cl, 
        cl_2
    ])
 
    page.add(row)
    page.add(tomzinha_name)

    while True:
        data = loads(queue.get())
        cl.height = page.window.height - 70
        cl.width = page.window.width

        t2.value = tr_ob.current_english_text

        if 'partial' in data and data["partial"] != "":
            t.value = data['partial']
            queue_translator.put(t.value)
            page.update()


def translate_text_rotine():
    while True:
        d = queue_translator.get()
        if d != "":
            tr_ob.current_english_text = tr_ob.translate(d)
        

thread = Thread(target=start_ai_voice)
thread.start()


thread_2 = Thread(target=translate_text_rotine)
thread_2.start()


ft.app(start_gui)