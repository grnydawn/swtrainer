#!/bin/bash

SWT_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

source ${SWT_HOME}/bin/env.sh

pip $*
