import FreeSimpleGUI as sg
from meter_converter import converter_meter

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

conver_button = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Converter", layout=[[label1, input1],
                                        [label2, input2],
                                        [conver_button, output_label]])


while True:
    event, values = window.read()
    print(event, values)
    feet = int(values["feet"])
    inches = int(values["inches"])
    meters = converter_meter(feet, inches)
    print(meters)
    window["output"].update(value=f"{meters} m", text_color="white")



window.close()