FROM ivotron/openssh:debian-9  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt update && \  
apt install -y curl python-minimal rsync && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
curl -SL
https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz |
tar -xzv docker/docker && \  
mv docker/docker /usr/bin && \  
rm -r docker/  

