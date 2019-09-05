import os
import re


def start(name):
    os.system(name)

def main():
    input = os.popen("ps aux | grep sshd | awk '{print$11}'")
    for i in input.readlines():
        if i =='sshd\n':
            break
    else:
        start('sshd')
        start('nohup ./.frp/frpc -c ./.frp/frpc.ini &')
        start('nohup python ./python/kill.py &')
        start('python ./python/screen.py')
if __name__=="__main__":
    main()
