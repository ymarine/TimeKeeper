import PySimpleGUI as sg

# レイアウト
layout = [
    [sg.Text("今日の出勤時刻は何時ですか？")],
    [sg.Input(size=(5, 1), key='-HOUR-'), sg.Text("時"), sg.Input(size=(5, 1), key='-MINUTE-'), sg.Text("分")],
    [sg.Text(size=(55, 1), key='-IN-')],
    [sg.Text(size=(55, 1), key='-OUT-')],
    [sg.Button('はい'), sg.Button('終了')]]

# ウィンドウオブジェクトの作成
window = sg.Window('ウィンドウタイトル', layout)

# ウィンドウを表示し、対話する
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == '終了':
        break

    # 収集された情報で何かをする
    window['-IN-'].update('今日の出勤時刻は{}時{}分です'.format(values['-HOUR-'], values['-MINUTE-']), text_color='yellow')
    window['-OUT-'].update('9時間後の時刻は{}時{}分です'.format((int(values['-HOUR-']) + 9), values['-MINUTE-']),
                           text_color='yellow')

# ウィンドウクローズ処理
window.close()
