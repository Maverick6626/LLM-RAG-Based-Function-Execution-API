import os
import webbrowser
import psutil
import subprocess

def open_chrome():
    webbrowser.open('http://www.google.com')
    print('Chrome opened successfully')

def open_calculator():
    os.system('calc')
    print('Calculator opened successfully')

def open_notepad():
    os.system('notepad')
    print('Notepad opened successfully')

def use_powershell(dict):
    cmd = "Write-Host 'Hello World!'" # Command to be executed
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    dict['powershell_output'] = completed.stdout.decode('utf-8')
    print('Powershell executed successfully')

def cpu_usage(dictionary_):
    usage = str(psutil.cpu_percent(interval=1)) + '%'
    dictionary_['cpu_usage'] = usage
    print('CPU Percentage :', usage)

def memory_usage(dictionary_):
    usage =  str(psutil.virtual_memory()[2]) + '%'
    dictionary_['memory_usage'] = usage
    print('RAM Usage :', usage)

def disk_usage(dictionary_):
    usage = str(psutil.disk_usage('/')[-1]) + '%'
    dictionary_['disk_usage'] = usage
    print('Disk Usage :', usage)

# Test run
if __name__=='__main__':
    dictionary_ = {}
    cpu_usage(dictionary_)
    memory_usage(dictionary_)
    disk_usage(dictionary_)
    print(dictionary_)