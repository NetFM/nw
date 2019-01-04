#!/bin/bash

rsync -r dave@big5.netfm.org:/home/nw/media /home/nw/

cp /home/nw/db.sqlite3 /home/nw/db.sqlite3-old
rsync dave@big5.netfm.org:/home/nw/db.sqlite3 /home/nw/


