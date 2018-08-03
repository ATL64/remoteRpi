import subprocess
import sys

file_path=sys.argv[1]

file = open(file_path,"r")

text = file.read()

signals_raw = text.split("Raw code:")

signals_raw.pop(0)

for i in range(len(signals_raw)):
    keep_string = signals_raw[i].split('\n')[1]
    keep_string = 'pilight-send -p raw -c "' + keep_string + '" \n'
    subprocess.run(keep_string, shell=True, check=True)