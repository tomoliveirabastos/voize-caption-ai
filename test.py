from argostranslate import translate

def translate_to_portuguese(text: str) -> str:
    from_code = 'en'
    to_code = 'pt'    

    print(text, from_code, to_code)
    return translate.translate(text, from_code, to_code)

a = translate_to_portuguese("Hello")

print(a)