import pyperclip
import keyboard, pyautogui, time

def simulate_typing(text):
    initial_delay = .5
    typing_delay = 0.01
    # Activate the text input field
    # pyautogui.click()
    time.sleep(initial_delay)
    # Type out the text character by character
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(typing_delay)     
    print('done!')
    main()

def main():
    print("[ to start typing from the clipboard.")
    thing = input('keyboard or pyauto?: ')
    clipboard_text = pyperclip.paste()
    if 'k' in thing.lower():
        print('Using keyboard! \n')
        keyboard.wait('[')
        keyboard.write(clipboard_text)
        print('pasted!')
        main()
    else:
        while True:
            keyboard.wait('[')
            simulate_typing(clipboard_text)
            print('pasted!')

if __name__ == '__main__':
    main()
    print('started!')
