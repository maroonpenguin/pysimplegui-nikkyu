import PySimpleGUI as sg

# sg.Frameでフレームを定義
frame1 = sg.Frame('',
                  [
                      [sg.Text('日給計算アプリ')],
                      [sg.Text('開始時間', size=(10, 1)), sg.InputText('09:00')],
                      [sg.Text('終了時間', size=(10, 1)), sg.InputText('17:00')],
                      [sg.Text('休憩時間', size=(10, 1)), sg.InputText('1:00')],
                      [sg.Text('時給', size=(10, 1)), sg.InputText('1100')],
                      [sg.Text('出勤日数', size=(10, 1)), sg.InputText('20')],
                      [sg.Submit(button_text='計算')]
                  ], size=(200, 200)
                  )
frame2 = sg.Frame('',
                  [
                      [sg.Text('日給')],
                      [sg.Input('', disabled=True, key='-DAY-')],
                      [sg.Text('月給')],
                      [sg.Input('', disabled=True, key='-MONTH-')],
                      [sg.Text('年収')],
                      [sg.Input('', disabled=True, key='-YEAR-')],
                  ], size=(100, 200)
                  )

# 画面レイアウトを指定
layout = [
    [frame1, frame2]
]

# ウィンドウを表示する関数


def show_window():
    window = sg.Window('日給計算', layout)
    # イベントループ
    while True:
        event, values = window.read()
        if event is None:
            break
        if event == '計算':
            # ここで日給を計算
            # calc_payment(values)
            start_t = timestr_to_min(values[0])
            end_t = timestr_to_min(values[1])
            rest_t = timestr_to_min(values[2])
            jikyu = values[3]
            day = values[4]
            # 取得した値から時給を計算
            m = (end_t - start_t - rest_t)
            val_d = int((m / 60) * float(jikyu))
            val_m = val_d * int(day)
            val_y = val_m * 12
            # 結果を表示
            window['-DAY-'].update("{:,}".format(val_d) + "円")
            window['-MONTH-'].update("{:,}".format(val_m) + "円")
            window['-YEAR-'].update("{:,}".format(val_y) + "円")


# HH:MMの形式を分に変換


def timestr_to_min(hm):
    h, m = hm.split(":")  # 時と分に分ける
    return int(h) * 60 + int(m)


show_window()
