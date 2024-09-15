import FreeSimpleGUI as sg
from meter_converter import converter_meter

sg.theme("Black")

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

conver_button = sg.Button("Convert")
output_label = sg.Text(key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Converter", layout=[[label1, input1],
                                        [label2, input2],
                                        [conver_button, output_label],
                                        [exit_button]])


while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    try:
        feet = int(values["feet"])
        inches = int(values["inches"])
        meters = converter_meter(feet, inches)
        window["output"].update(value=f"{meters} m", text_color="white")
    except ValueError:
        sg.popup("Enter a number first for feet and inches.", font=('Helvetica', 10))



window.close()