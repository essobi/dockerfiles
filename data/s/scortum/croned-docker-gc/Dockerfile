FROM alpine:3.4  
MAINTAINER Alex  
  
  
RUN apk update \  
&& apk upgrade \  
&& apk add \  
bash \  
curl \  
dcron \  
git \  
&& rm -rf /var/cache/apk/*  
  
# from https://github.com/spotify/docker-gc/blob/master/Dockerfile  
ENV DOCKER_VERSION 1.12.1  
RUN cd /tmp/ \  
&& curl -sSL -O
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz \  
&& tar zxf docker-${DOCKER_VERSION}.tgz \  
&& mkdir -p /usr/local/bin/ \  
&& mv $(find . -type f -name 'docker') /usr/local/bin/ \  
&& chmod +x /usr/local/bin/docker \  
&& curl -sSL -O https://raw.githubusercontent.com/spotify/docker-
gc/master/docker-gc \  
&& mv docker-gc /usr/local/bin/ \  
&& chmod +x /usr/local/bin/docker-gc \  
&& apk del curl \  
&& rm -rf /tmp/*  
  
COPY container-content/entry.sh /  
COPY container-content/cronjob.config /  
  
CMD ["/entry.sh"]  
  

