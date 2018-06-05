FROM docker:latest  
  
ARG PUID=1000  
ARG DOCKER_MACHINE_VERSION=v0.13.0  
  
RUN apk --no-cache add \  
bash \  
curl \  
jq \  
git \  
openssh-client \  
python \  
py-pip \  
python-dev \  
&& pip install docker-compose awscli \  
&& aws --version \  
&& curl -L
https://github.com/docker/machine/releases/download/${DOCKER_MACHINE_VERSION}/docker-
machine-`uname -s`-`uname -m` >/tmp/docker-machine \  
&& chmod +x /tmp/docker-machine && cp /tmp/docker-machine
/usr/local/bin/docker-machine \  
&& docker-machine --version \  
&& adduser -D -u ${PUID} -G ping -h /home/nonroot nonroot  
  
USER nonroot  

