#!/bin/bash -l
# qsub job body invoked by submit.sh via `-v REPO_DIR=...,JOB_CMD=...`.
# Not meant to be run directly.
set -euo pipefail
cd "$REPO_DIR"
eval "$JOB_CMD"
