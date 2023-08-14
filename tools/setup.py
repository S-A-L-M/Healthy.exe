from setuptools import setup, find_packages

setup(
    name='keylogger_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pynput',
        'watchdog',
        'pyperclip',
        'pywin32',
        'psutil',
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'keylogger = keylogger_app.keylogger:main',
        ],
    },
)
