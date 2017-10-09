#!/usr/bin/sh

# configure postgre SQL

DB_FOUND=0

# make sure it's installed first
if hash psql 2>/dev/null; then
  echo "postgre found"
  DB_FOUND=1
else
  echo "ERROR: postgre not found (are you sure it's installed?)"
  exit
fi

if [ "$DB_FOUND" -eq 1 ]; then
  # config the database from file
  psql -f ./setup_cmds.sql
  echo "yo yo yo "
  # change back to root
  exit
fi
