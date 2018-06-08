FROM alpine:3.4  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
RUN set -x && apk add --no-cache --virtual curl && \  
curl -L https://github.com/docker/machine/releases/download/v0.7.0/docker-
machine-Linux-x86_64 >/usr/local/bin/docker-machine && \  
chmod +x /usr/local/bin/docker-machine && \  
curl -L https://github.com/yamamoto-febc/docker-machine-
sakuracloud/releases/download/v0.0.11/docker-machine-driver-sakuracloud-
Linux-x86_64 >/usr/local/bin/docker-machine-driver-sakuracloud && \  
chmod +x /usr/local/bin/docker-machine-driver-sakuracloud  
  
ENTRYPOINT ["/usr/local/bin/docker-machine"]  
CMD ["--help"]  

