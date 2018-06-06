FROM alpine:3.4  
  
ENV MAX_CONTAINER_AGE=30days MAX_IMAGE_AGE=30days RUN_INTERVAL=daily
DOCKER_DIR=/var/lib/docker DOCKER_SOCK=/var/run/docker.sock
REMOVE_VOLUMES="false" VOLUME_FILTER="dangling=true"  
RUN set -e \  
&& apk add \--update docker \  
&& mkdir -p /etc/periodic/  
  
ADD rootfs /  
  
RUN chmod +x /init /job  
  
CMD ["/init"]  

