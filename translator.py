from googletrans import Translator
import sys
from googletrans.constants import LANGCODES


def translate() -> None:
    translator = Translator()
    while True:
        text = input("Please enter the text to be translated: ")
        trans_lang = input(
            "Please enter the language you want to translate the text to: ")
        try:
            lang = "en" if trans_lang == "" or trans_lang == None else LANGCODES[trans_lang.lower(
            )]
            translate = translator.translate(text, dest=lang)
            print(translate.text)
        except Exception:
            print(
                f"Error when translating the text: {sys.exc_info()[0].__doc__}")
        choice = int(
            input("Press 1 to translate again, 2 to quit the program: "))
        if choice == 1:
            continue
        elif choice == 2:
            print("Thank you for using the translator program")
            break
        else:
            print(
                "Wrong Choice, Please try again later. Thank you for using the translator program")
            break


if __name__ == "__main__":
    translate()
