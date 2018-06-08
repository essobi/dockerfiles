FROM debian:wheezy  
MAINTAINER Pomin Wu <pomin5@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV REFRESHED_AT 2014-12-08  
RUN apt-get update && \  
apt-get install -yq openssh-server sudo pwgen && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN mkdir /var/run/sshd # privilege separation directory required by sshd  
  
RUN groupadd -g 1000 app && \  
useradd -u 1000 -g app --home-dir /app -m app  
  
VOLUME ["/root", "/app"]  
  
ADD init.sh /init.sh  
ADD run.sh /run.sh  
  
EXPOSE 22  
CMD ["/run.sh"]  

