FROM alpine:3.4  
RUN apk --update add --no-cache curl ca-certificates && \  
curl -L https://github.com/docker/machine/releases/download/v0.10.0/docker-
machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine && \  
chmod +x /usr/local/bin/docker-machine && \  
apk del --purge curl  
  
RUN mkdir -p /var/d-machine  
  
ENV MACHINE_STORAGE_PATH="/var/d-machine"  
VOLUME /var/d-machine  
  
ENTRYPOINT [ "docker-machine"]  
CMD [ "version" ]  

