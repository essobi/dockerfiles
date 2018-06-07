FROM alpine:3.4  
RUN \  
apk update && \  
apk upgrade && \  
apk add docker && \  
true  
ENTRYPOINT \  
export DOCKER_API_VERSION=1.22 && \  
docker volume ls -q | while read VOLUME; do docker run \--interactive --rm
--volume ${SOURCE}:/source:ro alpine:3.4 [[ ! -d /source/${VOLUME} ]] &&
docker volume rm ${VOLUME}; done && \  
docker run \--interactive --rm --volume ${SOURCE}:/source:ro --privileged
alpine:3.4 ls -1 /source | while read VOLUME; do docker volume create --name
${VOLUME}; done && \  
docker run \--interactive --tty --rm --volume ${SOURCE}:/source:ro $(docker
volume ls -q | while read VOLUME; do echo " --volume
${VOLUME}:/destination/${VOLUME}:rw "; done) --privileged
emorymerryman/rsync:1.0.0 --verbose --archive --delete --progress /source/
/destination && \  
true  

