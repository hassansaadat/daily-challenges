#!/bin/bash

# Variables
DB_NAME=mydatabase
DB_USER=myuser
TIMESTAMP=$(date +%Y%m%d%H%M%S)
BACKUP_FILE=backup_${DB_NAME}_${TIMESTAMP}.sql.gz
S3_BUCKET=mystorage/mybucket

# Perform the backup
pg_dump -U ${DB_USER} -d ${DB_NAME} | gzip | mc pipe $S3_BUCKET/${BACKUP_FILE}
