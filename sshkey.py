#!python

# Written by Thiago Linhares
# 09/14/2017
#
# Basic script to retrieve SSH Public key from URL and append (or create) to existing authorized_keys
# Ideally built to be run using "curl https://thiagolinhares.github.io/sshkey/sshkey.py | python -"
#

import os
import os.path
import urllib
import sys
import shutil

destination = "/tmp/public_key"
if os.path.exists(destination) is False:
        os.mkdir(destination)
urllib.urlretrieve("https://www.fixit.inf.br/downloads/files/01-linhares-pubkey", os.path.join(destination, "01-linhares-pubkey"))

pubkey=open("/tmp/public_key/01-linhares-pubkey", "r")
contents =pubkey.read()
print "CHAVE SSH:\n",contents
sshfolder = "/root/.ssh"
if os.path.exists(sshfolder) is False:
        os.mkdir(sshfolder)
sshkeys=open("/root/.ssh/authorized_keys", "a+")
sshkeys.write(contents)
shutil.rmtree(destination)
