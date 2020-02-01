#!/bin/bash
set -eu
#### "Magic starts Here" - H. Potter #####
### Install themes
if [[ ${ADD_MODULES} != 'false' ]]; then
  echo "Installing additional modules: ${ADD_MODULES}"
  pip install -q ${ADD_MODULES}
fi

check_install_status () {
  if [[ ! -e /workdir/mkdocs ]]; then
    echo "No documentation folder available. Creating new one."
    mkdir -p /workdir/mkdocs
  fi
  cd /workdir/mkdocs
  if [[ ! -e "mkdocs.yml" ]]; then
    echo "No previous config. Starting fresh instalation"
    mkdocs new .
  fi
}
start_mkdocs () {
  if [[ ${LIVE_RELOAD_SUPPORT} != 'true' ]]; then
    echo "[ DISABLED ] - livereload"
    LRS='--no-livereload'
  else
    echo "[ ENABLED ] - livereload"
    LRS=''
  fi
  cd /workdir/mkdocs
  echo "Starting MKDocs"
  mkdocs serve -a 0.0.0.0:8000 $LRS
}

get_docs () {
  if [[ ! -e /workdir/mkdocs ]]; then
    echo "Downloading documentation from Git Repository"
    git clone ${GIT_REPO} /workdir/mkdocs
  fi
}

if [ ${GIT_REPO} != 'false' ]; then
  get_docs
  start_mkdocs
else
  check_install_status
  start_mkdocs
fi
