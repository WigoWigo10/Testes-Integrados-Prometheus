# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('app.exe', '.'),
        ('tesk.ico', '.'),

        ('ac_test.py', '.'),
        ('AC_TestedeAtivacao.bat', '.'),

        ('fan_test.py', '.'),
        ('Fan_TestedeAtivacao.bat', '.'),

        ('hdmi_test.py', '.'),
        ('HDMI_TestedeAtivacao.bat', '.'),

        ('keyboardscan_test.py', '.'),
        ('Keyboard_TestedeAtivacao.bat', '.'),
        ('tecla.json', '.'),
        ('keyboard.json', '.'),

        ('lid_test.py', '.'),
        ('LID_TestedeAtivacao.bat', '.'),

        ('touch_test.py', '.'),
        ('TouchEmulator_TestedeAtivacao.bat', '.'),
        ('touch.json', '.'),

        ('MainWindow.ui', '.'),
        ('MainWindow.py', '.'),


    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Rotina de Testes de Loop',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='tesk.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True,  # Isso indica que queremos um único arquivo executável
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='TestecomDiretorioeFrontV6.0',
)
