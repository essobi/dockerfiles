#appertly/meanjs is basic mean-stack install application meant to be run along
side mongodb  
#it includes angular cli and nodemon for development  
  
FROM ubuntu:latest  
MAINTAINER Stephanie McLaren  
  
EXPOSE 80 443 4200 35729 8080  
  
ENV NODE_ENV development  
  
RUN apt-get update -q \  
&& apt-get install -yqq \  
curl \  
git \  
ssh \  
gcc \  
make \  
build-essential \  
libkrb5-dev \  
sudo \  
apt-utils \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN sudo apt-get install -yq nodejs \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install --global nodemon --global @angular/cli --global foreman  
  
RUN mkdir -p /opt/mean.js/public/lib  
ADD start.sh /scripts/start.sh  
RUN chmod +x /scripts/start.sh  
WORKDIR /opt/mean.js  
  
CMD ["/scripts/start.sh"]

