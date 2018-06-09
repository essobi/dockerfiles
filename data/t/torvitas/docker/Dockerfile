FROM ubuntu:16.04  
MAINTAINER docker@saschaschmidt.net  
  
# Install Docker and dependencies  
RUN apt-get update -qq; apt-get install -qqy \  
curl \  
make \  
python-pip \  
git \  
supervisor \  
sudo \  
&& apt-get clean \  
&& pip install --upgrade docker-compose pip \  
&& rm -rf /root/.cache/pip/*  
  
RUN curl -sSL https://get.docker.com/ | sh  
  
VOLUME /var/lib/docker  
ENTRYPOINT ["dockerd-entrypoint.sh"]  
CMD '/bin/bash'  
RUN mkdir -p /var/log/docker  
  
COPY src/ /usr/local/  

