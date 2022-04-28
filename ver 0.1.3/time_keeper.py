import PySimpleGUI as sg
import datetime

todayDetail = datetime.datetime.today()

# レイアウト
layout = [
    [sg.Text("今日の出勤時刻は何時ですか？")],
    [sg.Input(todayDetail.hour, size=(3, 1), key='-HOUR-'), sg.Text("時"),
     sg.Input(todayDetail.minute, size=(3, 1), key='-MINUTE-'), sg.Text("分")],
    [sg.Button('Now'), sg.Button('Clear')],
    [sg.Button('出勤')],
    [sg.Text(size=(55, 1), key='-IN-')],
    [sg.Text(size=(55, 1), key='-OUT-')],
    [sg.Button('終了')]]

# ウインドウサイズ
win_size = (250, 220)

# ウィンドウオブジェクトの作成
window = sg.Window('TimeKeeper', layout, resizable=True, size=win_size)

# ウィンドウを表示し、対話する
while True:
    event, values = window.read()

    if event == 'Now':
        window['-HOUR-'].update(todayDetail.hour)
        window['-MINUTE-'].update(todayDetail.minute)
    elif event == 'Clear':
        window['-HOUR-'].update("")
        window['-MINUTE-'].update("")
    elif event == sg.WINDOW_CLOSED or event == '終了':
        break

    # 収集された情報で何かをする
    window['-IN-'].update('今日の出勤時刻は{}時{}分です'.format(values['-HOUR-'].zfill(1), values['-MINUTE-'].zfill(1)))
    window['-OUT-'].update('9時間後の時刻は{}時{}分です'.format((int(values['-HOUR-'].zfill(1)) + 9), values['-MINUTE-'].zfill(1)),
                           text_color='yellow')

# ウィンドウクローズ処理
window.close()
