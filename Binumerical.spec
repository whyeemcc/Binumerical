# -*- mode: python -*-

block_cipher = None


a = Analysis(['Main.py'],
             pathex=['D:\\Program Files\\Python\\Python36-32\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'D:\\GitHub\\Binumerical'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Binumerical',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='D:\\GitHub\\Binumerical\\images\\logo.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Binumerical')
