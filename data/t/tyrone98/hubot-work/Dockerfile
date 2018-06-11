FROM node:latest  
  
MAINTAINER tyrone  
  
RUN adduser \--disabled-password \--gecos "" yeoman \  
&& apt-get -q update \  
&& apt-get -qy install git-core redis-server \  
&& npm install -g yo generator-hubot coffee-script \  
&& curl -sSL https://get.docker.com/builds/Linux/x86_64/docker-1.11.1.tgz -o
/tmp/docker.tgz \  
&& tar zxf /tmp/docker.tgz -C /tmp \  
&& cp /tmp/docker/docker /usr/bin/docker \  
&& chmod +x /usr/bin/docker \  
&& curl -sSL -k https://dl.bintray.com/docker-compose/master/docker-compose-
Linux-x86_64 > /usr/bin/docker-compose \  
&& chmod +x /usr/bin/docker-compose \  
&& curl -sSL -k
https://github.com/docker/machine/releases/download/v0.6.0/docker-machine-
Linux-x86_64 > /usr/bin/docker-machine \  
&& chmod +x /usr/bin/docker-machine \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER yeoman  
ENV HOME /home/yeoman  
WORKDIR /home/yeoman  
  
RUN git clone https://github.com/baoquan-hq/hubot-work.git hubot && cd hubot
&& npm install  
  
CMD cd hubot; bin/hubot \--adapter slack  
  

