#!/bin/bash
set -eu
#### "Magic starts Here" - H. Potter #####
check_install_status () {
    cd /workdir/mkdocs
    if [[ ! -e "mkdocs.yml" ]]; then
    echo "No previous config. Starting fresh instalation"
    mkdocs new .
    fi
}
start_mkdocs () {
    cd /workdir/mkdocs
    echo "Starting MKDocs"
    mkdocs serve -a $(ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1):8000
}

get_docs () {
    echo "Downloading documentation from Git Repository"
    git clone ${GIT_REPO} /workdir/mkdocs
}

if [ ${GIT_REPO} != 'false' ]; then
    get_docs
    start_mkdocs
else
    check_install_status
    start_mkdocs
fi