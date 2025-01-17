from argostranslate import translate

class TranslateObject:

    def __init__(self):
        self.from_code = 'en'
        self.to_code = 'pt'
        self.current_english_text = ""


    def translate(self, english_text: str) -> str:
        print(self.from_code, self.to_code)
        self.current_english_text = translate.translate(english_text, self.from_code, self.to_code)
        return self.current_english_text