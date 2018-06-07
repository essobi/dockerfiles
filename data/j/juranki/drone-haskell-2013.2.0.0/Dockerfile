FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
RUN apt-get -qqy update  
RUN apt-get -qqy install git git-core socat haskell-platform && \  
cabal update  
RUN apt-get -qqy install curl htop wget  
RUN curl -s https://get.docker.io/ubuntu/ | sh  
  
VOLUME /var/lib/docker  
  
RUN locale-gen en_US en_US.UTF-8 && dpkg-reconfigure locales  

