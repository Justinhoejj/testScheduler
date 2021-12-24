#! /bin/bash

echo $(
/usr/local/bin/python3 /Users/justinhoe/Desktop/Projects/scheduledTask/update.py
cd /Users/justinhoe/Desktop/Projects/scheduledTask
git add --all
git commit -m "Updated on $(date -u)"
git push origin master
)
