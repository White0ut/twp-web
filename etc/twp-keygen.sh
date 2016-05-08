#!/bin/bash

# twp-keygen - Manage student keys
#
# Facilitate the process of generating private/public RSA
# keys and sending them to the git server

if [[ ! -f ~/.ssh/id_rsa && ! -f ~/.ssh/id_rsa.pub ]] {
    ssh-keygen -b 2048 -t rsa -f ~/.ssh/id_rsa -q -N ""
}

exit 0
