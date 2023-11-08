# SIMPLE LOGGER FOR LOGGING STATES FROM WAR THUNDER

## 0. OVERVIEW

- This repository contains a code for building a container which logs [War Thunder](https://warthunder.com/en) sate data.
- It is possible with a Python library `WarThunder`.
- Log data will be saved as `write.csv`.
- Prebuilt image is available on [docker hub](https://hub.docker.com/r/kestr3l/warthunder-logger).

## 1. AVAILABLE IMAGES & BUILD ORDERS

### 1.1. IMAGE AVAILABILITY

|TAG|ARCH|AVAILABILITY|Misc.|
|:-|:-|:-:|:-|
|`dev`|AMD64|✅|-|

## 2. ENVIRONMENT VARIABLE SETUPS

|VAR|DESCRIPTION|EXAMPLE|Misc.|
|:-|:-|:-|:-|
|`HOST_IP_ADDR`|Private IP of a host running War Thunder.<br/>This IP must be accessible from the Docker host.|172.16.0.1|-|
## 3. HOW-TO-BUILD

```bash
DOCKER_BUILDKIT=1 docker build \
--build-arg BASEIMAGE=ubuntu \
--build-arg BASETAG=22.04 \
-t kestr3l/warthunder:dev \
-f ./Dockerfile .
```

## 4. HOW-TO-RUN

- Get a private IP address of a host running War Thunder
- If you want to make a logging data persistent, set data directoy and map
- Template of `docker run` command is suggested as following:

```shell
docker run -it -d --rm --net host \
-e HOST_IP_ADDR=<PRIVATE_IP_OF_HOST> \
-v <DIR_TO_SAVE_DATA>:/home/user/data \
--name warthunder-logger \
kestr3l/warthunder:dev
```