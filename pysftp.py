#本地上傳遠端 72-->67
import paramiko
import os

hostname = '192.168.88.67'
username = 'root'
password = 'Aa123456!'
port = 22## 下載檔案
t = paramiko.Transport((hostname, port))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)

# 通過 sftp 看遠端server 路徑有什麼文件
sftp.listdir('/tmp/data/input')

# 設置本地路徑:
local_dir ='c:\\b\\c.log'

# 設置遠程路徑:
remote_dir=r'/tmp/data/input/monitorData-cdatm.log'

# 下載遠端路徑文件到本地路徑
sftp.get(remote_dir, local_dir)

# 查看本地路徑文件是否成功下載下來
os.listdir(os.getcwd())

# 上傳檔案
t = paramiko.Transport((hostname, port))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(r'c:/log/monitorData-fiscIIEdc.log', r'/tmp/data/output/monitorData-fiscIIEdc.json')
t.close()




