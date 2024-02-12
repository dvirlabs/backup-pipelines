import subprocess

command = subprocess.run('curl -XGET -k -u dvir:Aa123456 https://5.29.128.192:9200/_ingest/pipeline')

print (command)