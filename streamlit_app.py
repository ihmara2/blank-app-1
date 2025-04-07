import streamlit as st
from music21 import converter, environment
from pathlib import Path
import random
import base64

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

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded_img = base64.b64encode(img_bytes).decode()
    return encoded_img

whole_note64 = img_to_bytes("notes/note_whole.jpg")
html = f"<a href='#'><img src='data:image/png;base64,{whole_note64}'></a>"
st.markdown(html, unsafe_allow_html=True)

left, middle, right = st.columns(3)
if left.button("![ц]({html}) Целая нота", use_container_width=True):
    left.markdown("You clicked the plain button.")
#https://www.dropbox.com/scl/fi/d34b12gp4jkl73b66k3lj/note_half_dot.jpg?rlkey=k4yg3sl5saij3gkyuqeyegxz4&dl=1
if middle.button("![пт](https://thumb.cloud.mail.ru/weblink/thumb/xw1/26NU/2DAwX4sb7) Половина с точкой", use_container_width=True):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")

container = st.container(border=True)
imageWhole, buttonWhole, imageHalf, buttonHalf = container.columns(4)
imageWhole.image("notes/note_whole.jpg", caption="", width = 3, use_column_width=False)
imageHalf.image("notes/note_half.jpg", caption="")
if buttonWhole.button("Целая нота", use_container_width=True):
    buttonWhole.markdown("You clicked the Целую нота")
if buttonHalf.button("Половинная нота", use_container_width=True):
    buttonHalf.markdown("You clicked the Половинная нота")

button_names = ["Целая нота", "Половинная нота"]
for button_name in button_names:
    col1, col2 = st.columns(2, vertical_alignment='center')
    col1.image("notes/note_whole.jpg", width=40)
    if col2.button("Целая нота"):
        col2.markdown("You clicked the Целую нота")

string_size = "100/1"
# ABC notation string
abc_string = "X: 1 \nM: {} \nK: C \n z/4".format(string_size)
#C D E G | G x X A z3 B Z c | "?"A [K:F] Z "?"X B | [K:A] A/4 A/2 A/ A A2 A3 A4 A6 A7 A8 A12 |
#A/4 A2 A/2 A C A A2 A3 A4 A6 A7 A8 A12

#us = environment.UserSettings()
#us['lilypondPath'] = '/home/vscode/.local/lib/python3.11/site-packages/lilypond-binaries/bin/lilypond'
#print(us['lilypondPath'])

# Parse the ABC notation
abc_score = converter.parse(abc_string, format='abc')
# Create a graph of the score
#thePlot = abc_score.plot('pianoroll', doneAction=None)

output_path = Path('test3')
abc_score.write(fmt="lily.png", fp=output_path)

st.image("test3.png", caption="Sunrise by the mountains")