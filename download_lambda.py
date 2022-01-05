import json
import subprocess
import os

def download_code(OUTPUT, COUNT):
    CMD = "aws lambda get-function --function-name {0} --query 'Code.Location' | xargs wget -O ./lambda_functions/{0}.zip".format(OUTPUT)
    print('Start download {0} = {1}'.format(COUNT, OUTPUT))
    os.system(CMD)


count = 1 
output = subprocess.check_output("aws lambda list-functions", shell=True)
DATA = json.loads(output)

with open('data_file.json', 'w', encoding='utf-8') as f:
    json.dump(DATA, f, ensure_ascii=False, indent=4)

for i in DATA['Functions']:
    __NAME = i['FunctionName']
    download_code(__NAME, count)
    count += 1
 