FROM debian:unstable  
MAINTAINER Tyler Ball <tyler@tylerball.net>  
RUN set -xe && \  
apt-get update && \  
apt-get -y install git man git-annex openssh-server  
RUN \  
useradd -u 1000 -U -d /home/git -s /usr/bin/git-annex-shell git && \  
mkdir -p /home/git/.ssh  
EXPOSE 22  
VOLUME ["/data", "/home/git/.ssh"]  
WORKDIR /data  
CMD service ssh start && while true; do sleep 3000; done  

