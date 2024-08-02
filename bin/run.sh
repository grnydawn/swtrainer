#!/bin/bash

SWT_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

source ${SWT_HOME}/bin/env.sh

python ${SWT_HOME}/src/iterative_improvement_with_finetuning.py
