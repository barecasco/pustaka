import socket
import os

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

os.system('cmd /k "python -m http.server 4000 --bind={}"'.format(host_ip))
