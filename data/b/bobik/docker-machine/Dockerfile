FROM alpine:edge  
  
ENV DOCKER_MACHINE_NAME=default  
ENV DOCKER_MACHINE_PORT=2376  
RUN apk add --no-cache bash docker curl openssh-client py2-pip  
  
RUN pip install docker-compose \  
&& docker-compose --version  
  
RUN DOWNLOAD_URL=$(curl -s
https://api.github.com/repos/docker/machine/releases | grep
browser_download_url | cut -d '"' -f 4 | grep -m 1 docker-machine-`uname
-s`-`uname -m`) \  
&& curl -L $DOWNLOAD_URL > /usr/bin/docker-machine \  
&& chmod +x /usr/bin/docker-machine \  
&& docker-machine --version  
  
RUN pip install awscli \  
&& aws --version  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

