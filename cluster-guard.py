import psutil
from signal import SIGKILL
import time
from datetime import datetime

# the uid is provided by IPA

for pp in psutil.process_iter(['pid', 'name', 'username', 'uids', 'cpu_percent', 'cpu_times', 'memory_full_info']):
    if pp.uids().real > 50000000:
        if pp.memory_full_info().rss / 1024. / 1024. > 20000:
            print(pp.name(), pp.username(), "large memory")

time.sleep(1)

white_list = ['sshd', 'bash', 'rsync']

for pp in psutil.process_iter(['pid', 'name', 'username', 'uids', 'cpu_percent', 'cpu_times', 'memory_full_info']):
    if pp.uids().real > 50000000 and pp.name() not in white_list:
        try:
            dstring = datetime.now().isoformat()
            # kill process consumes too much memory
            if pp.memory_full_info().rss / 1024. / 1024 > 20000:
                print(dstring, pp.name(), pp.username(), "large memory",
                      pp.memory_full_info.rss/1024/1024, "try kill it." )
                pp.send_signal(SIGKILL)
                continue
            cp = pp.cpu_percent(0.1)
            pct = pp.cpu_times()
            if cp > 95:
                # kill the process if it runs more than 900 s
                if pct.user > 900:
                    print(dstring, pp.name(), pp.username(), "cpu usage", cp,
                          "for", pct.user, "try kill it.")
                    pp.send_signal(SIGKILL) 
                else:
                    print(dstring, pp.name(), pp.username(), "cpu usage", cp,
                          "for", pct.user)

        except psutil.NoSuchProcess:
            pass
