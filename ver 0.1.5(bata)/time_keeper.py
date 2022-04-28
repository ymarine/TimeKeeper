import PySimpleGUI as sg
import datetime

import locale

locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")

time_in = datetime.datetime.today()


# 曜日の取得
def change_japanese_weekday(weekday):
    if weekday == 0:
        value = '月'
    elif weekday == 1:
        value = '火'
    elif weekday == 2:
        value = '水'
    elif weekday == 3:
        value = '木'
    elif weekday == 4:
        value = '金'
    elif weekday == 5:
        value = '土'
    elif weekday == 6:
        value = '日'
    else:
        value = '不明'

    return value


# 現在の時間の取得
def get_time_now():
    now = datetime.datetime.now()
    return now


# 時間の表示
def get_time():
    now = get_time_now()
    weekday_ja = change_japanese_weekday(now.weekday())
    time = now.strftime("%Y/%m/%d(" + weekday_ja + ") %H:%M:%S")
    window['-TIME-'].update(time)


# レイアウト
layout = [
    [sg.Text(size=(55, 1), key='-TIME-')],
    [sg.Text("今日の出勤時刻は何時ですか？")],
    [sg.Input(time_in.hour, size=(3, 1), key='-HOUR-'), sg.Text("時"),
     sg.Input(time_in.minute, size=(3, 1), key='-MINUTE-'), sg.Text("分")
        , sg.Button('Now'), sg.Button('Clear')],
    [sg.Button('出勤')],
    [sg.Text('今日の出勤時刻は', size=(55, 1), key='-IN-')],
    [sg.Text('退勤目安時刻は', size=(55, 1), key='-OUT-')],
    [sg.Button('終了')]]

# ウインドウサイズ
win_size = (250, 210)

# ウィンドウオブジェクトの作成
window = sg.Window('TimeKeeper', layout, resizable=True, size=win_size)

# ウィンドウを表示し、対話する
while True:
    event, values = window.read(timeout=100, timeout_key='-TimeOut-')

    if event == '-TimeOut-':
        get_time()
    elif event == 'Now':
        time_now = get_time_now()
        window['-HOUR-'].update(time_now.hour)
        window['-MINUTE-'].update(time_now.minute)
    elif event == 'Clear':
        window['-HOUR-'].update("")
        window['-MINUTE-'].update("")
    elif event == '出勤':
        if values['-HOUR-'].isdecimal():
            window['-IN-'].update('今日の出勤時刻は{}時{}分です'.format(values['-HOUR-'].zfill(1), values['-MINUTE-'].zfill(1)))
            window['-OUT-'].update(
                '退勤目安時刻は{}時{}分です'.format((int(values['-HOUR-'].zfill(1)) + 9), values['-MINUTE-'].zfill(1)),
                text_color='yellow')
        else:
            window['-IN-'].update('')
            window['-OUT-'].update('時刻が正しくありません', text_color='yellow')
    elif event == sg.WINDOW_CLOSED or event == '終了':
        break

# ウィンドウクローズ処理
window.close()
