#!/bin/bash
set -eu
#### "Magic starts Here" - H. Potter #####
check_install_status () {
    if [[ ! -e /workdir/mkdocs ]]; then 
        mkdir -p /workdir/mkdocs
    fi
    cd /workdir/mkdocs
    if [[ ! -e "mkdocs.yml" ]]; then
    echo "No previous config. Starting fresh instalation"
    mkdocs new .
    fi
}
start_mkdocs () {
    if [[ ${LIVE_RELOAD_SUPPORT} == 'true' ]]; then
        LRS='--no-livereload'
    else
        LRS=''
    fi
    cd /workdir/mkdocs
    echo "Starting MKDocs"
    mkdocs serve -a $(ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1):8000 $LRS
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