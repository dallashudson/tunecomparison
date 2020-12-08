# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Dallas\\Desktop\\tunedelta'],
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
d = Tree(os.getcwd() + '\\icons', prefix='icons')
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
	  d,
          name='Tune Differences Comparison',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False , icon='bomi.ico')
