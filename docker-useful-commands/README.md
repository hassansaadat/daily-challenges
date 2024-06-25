# Docker useful commands

## Remove orphan images
```bash
docker rmi $(docker images -f "dangling=true" -q)
```

## Remove orphan volumes
```bash
docker volume rm $(docker volume ls -f "dangling=true" -q)
```

## Remove all stopped containers
```bash
docker container prune
```

## Monitor all containers status
```bash
docker stats
```
