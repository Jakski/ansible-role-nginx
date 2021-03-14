#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

if ! systemctl is-active nginx >/dev/null; then
  echo "Service is not active."
  exit 1
fi
if ! systemctl is-enabled nginx >/dev/null; then
  echo "Service is not enabled."
  exit 1
fi
if ! nc -zw 1 127.0.0.1 80; then
  echo "127.0.0.1:80 is not listening for incoming connections."
  exit 1
fi
if ! wget http://127.0.0.1/ -qO - >/dev/null; then
  echo "Failed to fetch default website."
  exit 1
fi
if [ ! -f "/etc/nginx/nginx.conf" ]; then
  echo "/etc/nginx/nginx.conf file doesn't exist."
  exit 1
fi
if ! grep -qE '^worker_processes auto;$' "/etc/nginx/nginx.conf"; then
  echo "No worker_processes directive has been found in configuration file."
  exit 1
fi
