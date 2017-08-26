#!/bin/bash
set -eu
#### "Magic starts Here" - H. Potter #####
check_install_status () {
    if [[ ! -e "mkdocs.yml" ]]; then
    echo "No previous config. Starting fresh instalation"
    mkdocs new .
    fi
}
start_mkdocs () {
    echo "Starting MKDocs"
    mkdocs serve -a $(ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1):8000
}
check_install_status
start_mkdocs
