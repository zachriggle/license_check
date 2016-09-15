#!/usr/bin/env bash

DIR=$(mktemp -d)
virtualenv -q "$DIR"
source "$DIR/bin/activate"
pip install -q "$@"
pip freeze --local
rm -rf "$DIR"
