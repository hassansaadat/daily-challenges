# Postgres DB periodic backup

## Install minio client
```bash
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
sudo mv mc /usr/local/bin/
```

## Setup minio client
```bash
mc alias set <mystorage> https://s3.example.com <ACCESS-KEY> <SECRET-KEY>
```

## update backup.sh with proper variables

## make backup.sh executable
```bash
sudo chmod +x backup.sh
```

## add cronjob
```bash
sudo crontab -e
```

add this line:
```bash
0 0 * * * /home/<backupuser>/backup.sh >> /home/backupuser/backup.log 2>&1
```

## verify cronjob
```bash
sudo crontab -l
```

## view logs
```bash
tail -f /home/<backupuser>/backup.log
```


# Restore Database

You can simply restore database using this command:
```bash
psql -U postgres -d <mydatabase> -f /path/to/local/backup.sql
```
