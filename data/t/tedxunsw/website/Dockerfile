FROM ubuntu:16.04  
MAINTAINER JJ Lau <j.y.j.j.lau@gmail.com>  
  
RUN apt-get -yqq update \  
&& apt-get install -y curl language-pack-en\  
&& curl https://install.meteor.com/ | sh \  
&& apt-get autoclean \  
&& apt-get clean \  
&& apt autoremove  
  
#ENV METEOR_ALLOW_SUPERUSER=1  
RUN useradd --create-home --shell /bin/bash tedxunsw \  
&& echo 'tedxunsw:everythingisawesome' | chpasswd  
  
USER tedxunsw  
  
WORKDIR /home/tedxunsw  
  
EXPOSE 3000  

