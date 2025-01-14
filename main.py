from voice import VoiceAI
from threading import Thread
from queue import Queue
from json import loads
import flet as ft   


queue = Queue()


def start_ai_voice():
    ai = VoiceAI()
    ai.voice(lambda obj: queue.put(obj))


def start_gui(page: ft.Page):
    
    page.title = "TOMZINHA SUBTITLE AI"

    t = ft.Text(value="", size=25)
    
    page.window.height = 500
    page.window.width = 300
    
    cl = ft.Column(
        height=page.window.height - 70,
        width=page.window.width,
        scroll=ft.ScrollMode.ALWAYS,
        auto_scroll=True,
        adaptive=True,
    )
    cl.controls.append(t)
    tomzinha_name = ft.Text(value="contact: tomoliveira1995@gmail.com")
    
    page.add(ft.Container(cl, border=ft.border.all(1)))
    page.add(tomzinha_name)


    while True:
        data = loads(queue.get())
        cl.height = page.window.height - 70
        cl.width = page.window.width

        if 'partial' in data and data["partial"] != "":
            t.value = data['partial']        
            page.update()


thread = Thread(target=start_ai_voice)
thread.start()


thread = Thread(target=start_gui)
thread.start()

ft.app(start_gui)