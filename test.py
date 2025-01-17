from argostranslate import translate, package

def translate_to_portuguese(text: str) -> str:
    from_code = 'en'
    to_code = 'pt'    

    package.update_package_index()
    available_packages = package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    package.install_from_path(package_to_install.download())
    print(text, from_code, to_code)
    return translate.translate(text, from_code, to_code)

a = translate_to_portuguese("Hello")

print(a)