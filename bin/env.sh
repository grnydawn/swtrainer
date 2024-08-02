#!/bin/bash

SWT_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# check if venv is activated
if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "Virtual environment is activated."
else
    source ${SWT_HOME}/.venv/bin/activate
fi
