#!/bin/bash

# Define the main commands
MAIN_COMMANDS="--video --playlist --info --audio"

# Define the optional subcommands
VIDEO_SUBCOMMANDS="--ext --res"
PLAYLIST_SUBCOMMANDS="--ext --res"
INFO_SUBCOMMANDS="--res-only --ext-only"

# Get the video or playlist URL
URL="${2}"

# Build the Python command
PYTHON_COMMAND="python3 main.py"

# Add the main command and URL if they are passed
if [[ ! -z "${1}" ]]; then
  PYTHON_COMMAND="${PYTHON_COMMAND} ${1}"
fi

if [[ ! -z "${URL}" ]]; then
  PYTHON_COMMAND="${PYTHON_COMMAND} ${URL}"
fi

# Add any optional subcommands
if [[ "${1}" == "--video" || "${1}" == "--playlist" ]]; then
  if [[ ! -z "${3}" ]]; then
    PYTHON_COMMAND="${PYTHON_COMMAND} -e ${3}"
  fi

  if [[ ! -z "${4}" ]]; then
    PYTHON_COMMAND="${PYTHON_COMMAND} -r ${4}"
  fi
fi

if [[ "${1}" == "--info" ]]; then
  if [[ ! -z "${3}" ]]; then
    PYTHON_COMMAND="${PYTHON_COMMAND} -ro"
  fi

  if [[ ! -z "${4}" ]]; then
    PYTHON_COMMAND="${PYTHON_COMMAND} -eo"
  fi
fi

# Run the Python command
source .venv/bin/activate

echo $PYTHON_COMMAND

${PYTHON_COMMAND}

deactivate