import streamlit as st
from music21 import converter, environment
from pathlib import Path
import random
import base64

if 'result_notes' not in st.session_state:
    st.session_state['result_notes'] = ''

def get_size():
    string_array = ["2/2", "2/4", "3/4", "3/8", "4/4", "6/8", "5/4", "5/8", "7/4", "7/8", "4/1", "4/8", "6/4", "9/8", "12/8"]
    random_value = random.choice(string_array)
    return random_value

string_size = get_size()

def add_invite_header(string_size):
    numerator, denominator = string_size.split('/')
    numerator = int(numerator)
    denominator = int(denominator)
    formatted_string_size = u'{}\u2044{}'.format(numerator, denominator)
    st.header("Закончите такт, размер :blue[{}]:".format(formatted_string_size))

add_invite_header(string_size)

def createImage(notes):
    string_size = "100/1"
    abc_string = "X: 1 \nM: {} \nK: C \n {}".format(string_size, notes)
    abc_score = converter.parse(abc_string, format='abc')
    #C D E G | G x X A z3 B Z c | "?"A [K:F] Z "?"X B | [K:A] A/4 A/2 A/ A A2 A3 A4 A6 A7 A8 A12 |
#A/4 A2 A/2 A C A A2 A3 A4 A6 A7 A8 A12
    output_path = Path('test3')
    abc_score.write(fmt="lily.png", fp=output_path)
    st.image("test3.png", caption="Notes")
def calculateImageNote(newNote, existingNote):
    res_note = "{} {}".format(existingNote, newNote)
    return res_note

result_note = st.session_state['result_notes']

whole_note, half_dot_note, half_note, quater_dot_note, quater_note = st.columns(5)
if whole_note.button("![целая](https://thumb.cloud.mail.ru/weblink/thumb/xw1/PRpN/qbDRrxUn1) Целая нота", use_container_width=True):
    result_note = calculateImageNote("A12", result_note)
if half_dot_note.button("![половинная с точкой](https://thumb.cloud.mail.ru/weblink/thumb/xw1/VHpZ/peYuCrJBL) Половинная с точкой", use_container_width=True):
    result_note = calculateImageNote("A6", result_note)
if half_note.button("![половинная](https://thumb.cloud.mail.ru/weblink/thumb/xw1/Bip2/Huc2EyWqy) Половинная нота", use_container_width=True):
    result_note = calculateImageNote("A4", result_note)
if quater_dot_note.button("![четвертная с точкой](https://thumb.cloud.mail.ru/weblink/thumb/xw1/2Vcw/87xB2s8ou) Четвертная с точкой", use_container_width=True):
    result_note = calculateImageNote("A3", result_note)
if quater_note.button("![четвертная](https://thumb.cloud.mail.ru/weblink/thumb/xw1/hKUn/7BLwP4WaG) Четвертная нота", use_container_width=True):
    result_note = calculateImageNote("A2", result_note)

note8, note16, note32, note64, pause_whole = st.columns(5)
if note8.button("![восьмая](https://thumb.cloud.mail.ru/weblink/thumb/xw1/e3pf/Z9LbiG3d6) Восьмая нота", use_container_width=True):
    result_note = calculateImageNote("A", result_note)
if note16.button("![шестнадцатая](https://thumb.cloud.mail.ru/weblink/thumb/xw1/r2QW/ZZeJM1k3v) Шестнадцатая нота", use_container_width=True):
    result_note = calculateImageNote("A/2", result_note)
if note32.button("![32](https://thumb.cloud.mail.ru/weblink/thumb/xw1/xc7o/GetDZokC8) Тридцать вторая", use_container_width=True):
    result_note = calculateImageNote("A/4", result_note)
if note64.button("![64](https://thumb.cloud.mail.ru/weblink/thumb/xw1/rW8E/Ce5ZBCSpd) Шестьдесят четвёртая", use_container_width=True):
    result_note = calculateImageNote("A/8", result_note)
if pause_whole.button("![целая пауза](https://thumb.cloud.mail.ru/weblink/thumb/xw1/f2WC/btg7mn7Y2) Целая пауза", use_container_width=True):
    result_note = calculateImageNote("z8", result_note)

st.session_state['result_notes'] = result_note
createImage(result_note)