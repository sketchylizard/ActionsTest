#!/usr/bin/python3
import subprocess

arguments = ['build/tests', '-d', 'yes', '-r', 'xml']

output = subprocess.run(arguments, capture_output=True, text=True)
