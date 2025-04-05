import streamlit as st
from music21 import converter, environment
from pathlib import Path
import random

def get_size():
    string_array = ["2/2", "2/4", "3/4", "3/8", "4/4", "6/8", "5/4", "5/8", "7/4", "7/8", "4/1", "4/8", "6/4", "9/8", "12/8"]
    random_value = random.choice(string_array)
    return random_value

string_size = get_size()
string_size = "100/1"
# ABC notation string
abc_string = "X: 1 \nM: {} \nK: C \ns: !pp! ** !f! \nA/4 ||| A2 A/2 A/ **C !fff! A A2 A3 A4 A6 A7 A8 A12 ".format(string_size)
#C D E G | G x X A z3 B Z c | "?"A [K:F] Z "?"X B | [K:A] A/4 A/2 A/ A A2 A3 A4 A6 A7 A8 A12 |

us = environment.UserSettings()
us['lilypondPath'] = '/home/vscode/.local/lib/python3.11/site-packages/lilypond-binaries/bin/lilypond'
print(us['lilypondPath'])

# Parse the ABC notation
abc_score = converter.parse(abc_string, format='abc')
# Create a graph of the score
#thePlot = abc_score.plot('pianoroll', doneAction=None)

output_path = Path('test3')
abc_score.write(fmt="lily.png", fp=output_path)

st.image("test3.png", caption="Sunrise by the mountains")