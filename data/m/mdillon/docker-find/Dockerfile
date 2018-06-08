FROM debian:jessie  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -fSL https://get.docker.io | sh  
  
COPY docker-find /sbin/  
ENTRYPOINT ["docker-find"]  

