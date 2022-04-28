# coding: utf-8
# cx_Freeze 用セットアップファイル

import sys
from cx_Freeze import setup, Executable

file_path = "time_keeper.py"

base = None

# GUI=有効, CUI=無効 にする
if sys.platform == 'win32': base = 'Win32GUI'

excludes = [
    "numpy",
    "pandas",
    "lxml"
]

# exe にしたい python ファイルを指定
exe = Executable(script=file_path,
                 base=base)

# セットアップ
setup(name='TimeKeeper',
      options={
          "build_exe":
              {"excludes": excludes}
      },
      version='0.1',
      description='TimeKeeper',
      executables=[exe])
