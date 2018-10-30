#!/bin/bash
version=0
for file in ./*.sql
do
  version=$((version + 1)) 
  echo 'INSERT INTO testTable VALUES("this is version '${version}'");' > "$file"
done
