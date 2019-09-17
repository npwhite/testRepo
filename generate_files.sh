#!/bin/bash

if [ $1 == 'create' ]
then
    mkfile -n 2m junk_file
    
elif [ $1 == 'modify' ]
then
    echo "modifying..." | tee -a junk_file
fi
