FROM alpine:latest  
MAINTAINER waylybaye <baye@wayly.net>  
  
ENV DOCKER_HOST unix:///var/run/docker.sock  
ENV GIT_INTERVAL 300  
RUN apk --no-cache --update add openssh-client git python py-pip \  
&& rm -rf /var/cache/apk/* \  
&& pip install docker  
  
ADD main.py /opt/git-agent/main.py  
  
WORKDIR /opt/git-agent/  
VOLUME /rootfs/  
  
CMD python main.py /rootfs  

