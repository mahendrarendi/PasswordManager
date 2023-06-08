import sys
from cx_Freeze import setup, Executable

# File utama
main_script = 'main.py'

# Konfigurasi cx_Freeze
build_exe_options = {
    'packages': [],
    'excludes': [],
    'include_files': [
        ('logo.png', 'logo.png'),
        ('vault.csv', 'vault.csv'),
        #('/_pycache_', 'pycache'),
        ('get-pip.py', 'get-pip.py')
    ]
}

# Membuat executable
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'  # Untuk aplikasi GUI di Windows

executable = Executable(script=main_script, base=base)

# Setup
setup(
    name='Nama Aplikasi',
    version='1.0',
    description='Deskripsi Aplikasi',
    options={'build_exe': build_exe_options},
    executables=[executable]
)
