#!/bin/bash

if [ $1 == 'create' ]
then
    echo "Hello this is a sentence." | tee a.txt b.txt c.txt d.txt e.txt
elif [ $1 == 'modify' ]
then
    echo "Hello this is a sentence." | tee -a a.txt b.txt c.txt d.txt e.txt
fi
