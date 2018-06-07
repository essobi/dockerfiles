FROM ubuntu:16.04  
MAINTAINER Ian Martin <ian@imartin.net>  
  
RUN echo 'deb http://ppa.launchpad.net/stebbins/handbrake-releases/ubuntu
xenial main' > /etc/apt/sources.list.d/handbrake.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8771ADB0816950D8 && \  
apt-get update && \  
apt-get -y install handbrake-cli && \  
apt-get clean && \  
mkdir -p /media  
  
WORKDIR /media  
ENTRYPOINT ["HandBrakeCLI"]  
CMD ["--help"]  
  
VOLUME ["/media"]  

