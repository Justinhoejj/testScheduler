#! /bin/bash

#echo $(
# /usr/local/bin/python3 /Users/justinhoe/Desktop/Projects/scheduledTask/update.py
#)

echo $(
cd /Users/justinhoe/Desktop/Projects/scheduledTask
git add --all
git commit -m "$(date)"
git push
)
