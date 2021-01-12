Cluster Guard
=============

This project provides a small script together with Systemd configuration files to prevent users from running heavy tasks for long time on the interactive node of the cluster.

By default the script should be executed by root.

## Usage

The script requires `python3` and the `psutil` package. Please install the package before use it.

Put the python script in `/root/bin`.

Put the Systemd files in `/etc/systemd/system` and run

```bash
systemctl enable cluster_guard.timer
systemctl start cluster_guard.timer
```

Then the script will be executed every 2 minutes.

The output of the script will be sent to `syslog` and can be viewed with
```bash
journalctl -u cluster_guard`
```
