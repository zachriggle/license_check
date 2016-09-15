#!/usr/bin/env python2
import argparse
import os
import subprocess
import xmlrpclib

THIS_FILE = os.path.abspath(__file__)
THIS_DIR  = os.path.dirname(THIS_FILE)
SCRIPT    = os.path.join(THIS_DIR, 'check.sh')

parser = argparse.ArgumentParser()
parser.add_argument('package')

def check(package):
    output = subprocess.check_output([SCRIPT, package])
    client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
    releases = []

    for package in output.splitlines():
        name, version = package.split('==')
        release = client.release_data(name, version)
        print "{:>15}@{:<8} -- {}".format(name, version, release.get('license', '???'))

def main():
    args = parser.parse_args()
    return check(args.package)

if __name__ == '__main__':
    main()
