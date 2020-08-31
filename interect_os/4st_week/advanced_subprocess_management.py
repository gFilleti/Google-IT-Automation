#!/usr/bin/env python3.8

import os
import subprocess

my_env = os.environ.copy()#the copy method created a new dicionary that its a copy of the OSenviron dictionary
                          #With this new dictonay we can change as needed whithout modifying the original environment
                          #simulated envaironment
my_env["PATH"] = os.pathsep.join(['/opt/advanced_subprocess_manegement', my_env['PATH']])

result = subprocess.run(['advanced_subprocess_manegement'], env=my_env)
