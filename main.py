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
    
    page.title = "Voize Caption AI"

    t = ft.Text(value="", size=25)
    
    cl = ft.Column(
        height=page.window_height - 20,
        width=page.window_width,
        scroll=ft.ScrollMode.ALWAYS,
        auto_scroll=True,
        adaptive=True,
    )
    cl.controls.append(t)

    page.add(ft.Container(cl, border=ft.border.all(1)))

    while True:
        data = loads(queue.get())
        cl.height = page.window.height - 30
        cl.width = page.window.width

        if 'partial' in data and data["partial"] != "":
            
            print(data['partial'])
            t.value = data['partial']
        
            page.update()


thread = Thread(target=start_ai_voice)
thread.start()


thread = Thread(target=start_gui)
thread.start()

ft.app(start_gui)