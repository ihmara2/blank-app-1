import streamlit as st
from music21 import converter, environment
from pathlib import Path
import random

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

left, middle, right = st.columns(3)
if left.button("![ц](https://www.dropbox.com/scl/fi/63jqmvhyzmw4ajwwy9qlf/note_whole.jpg?rlkey=7ul4osvhguaitfpnx5qlvp3uq&dl=1) Целая нота", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("![пт](https://www.dropbox.com/scl/fi/d34b12gp4jkl73b66k3lj/note_half_dot.jpg?rlkey=k4yg3sl5saij3gkyuqeyegxz4&dl=1) Половина с точкой", use_container_width=True):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")


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