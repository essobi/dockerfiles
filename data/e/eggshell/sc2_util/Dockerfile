FROM ubuntu:xenial  
  
RUN export DEBIAN_FRONTEND="noninteractive" \  
&& apt-get update -qq && apt-get install -y apt-transport-https inotify-tools
software-properties-common \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial
main' \  
&& apt-get update -qq && apt-get install -y docker-engine \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY watch /usr/local/bin/watch  
  
CMD [ "watch" ]  

