import os
import sys
import subprocess

if not os.getuid() == 0:
    sys.exit("Error: Can only be executed by root")

services = ["cups", "cups.socket", "postgresql", "ssh", "vmware", "vmware-workstation-server"]

for service in services:
    subprocess.call(["systemctl", "stop", service])
