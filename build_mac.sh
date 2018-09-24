#!/usr/bin/env bash
chmod 777 scripts/reconstructDocument.py
cp  scripts/reconstructDocument.py reconstruct-document
#mkdir -p ~/bin
sudo mv reconstruct-document  /usr/local/bin/
#export PATH=$PATH":$HOME/bin"
