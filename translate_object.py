from argostranslate import translate, package

class TranslateObject:

    def __init__(self):
        self.from_code = 'en'
        self.to_code = 'pt'
        self.current_english_text = ""

    def install(self):

        package.update_package_index()
        available_packages = package.get_available_packages()
        package_to_install = next(
            filter(
                lambda x: x.from_code == self.from_code and x.to_code == self.to_code, available_packages
            )
        )
        package.install_from_path(package_to_install.download())



    def translate(self, english_text: str) -> str:

        self.current_english_text = translate.translate(english_text, self.from_code, self.to_code)
        return self.current_english_text