import psutil
import time

for pp in psutil.process_iter(['pid', 'name', 'username', 'uids', 'cpu_percent', 'cpu_times', 'memory_full_info']):
    if pp.uids().real > 50000000:
        if pp.memory_full_info().rss / 1024. / 1024. > 10000:
            print(pp.name(), pp.username(), "large memory")
            print(pp.memory_full_info().rss/1024./1024.)

time.sleep(1)
for pp in psutil.process_iter(['pid', 'name', 'username', 'uids', 'cpu_percent', 'cpu_times', 'memory_full_info']):
    if pp.uids().real > 50000000 and pp.name() not in ['sshd', 'bash', 'rsync']:
        if pp.memory_full_info().rss / 1024. / 1024. > 10000:
            print(pp.name(), pp.username(), "large memory", pp.memory_full_info().rss/1024./1024., "M")
        cp = pp.cpu_percent()
        if cp > 90 and pp.cpu_times().user > 600:
            print(pp.name(), pp.username(), "cpu usage", cp, "for",
                    pp.cpu_times())
            print(pp.cpu_times().user/60)
