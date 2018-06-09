FROM ubuntu:14.04  
MAINTAINER Takahiro Ooishi <taka0125@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends openssh-server supervisor vim git
build-essential libssl-dev zlib1g-dev ca-certificates  
  
# supervisor  
RUN mkdir -p /var/log/supervisor  
ADD supervisor.conf /etc/supervisor/conf.d/supervisord.conf  
  
# sshd  
RUN mkdir -p /var/run/sshd  
ADD supervisor-sshd.conf /etc/supervisor/conf.d/sshd.conf  
  
# add user  
RUN useradd -m docker -s /bin/bash  
RUN echo "docker:hw3TKfFBfvmPk4RdxaJkCazMJrbmKe" | chpasswd  
RUN echo "docker ALL=(ALL) ALL" > /etc/sudoers.d/docker  
  
# configure ssh for user  
RUN \  
mkdir -p /home/docker/.ssh && \  
chown docker:docker /home/docker/.ssh && \  
chmod 700 /home/docker/.ssh  
  
RUN apt-get clean  
  
CMD ["/usr/bin/supervisord"]  
  
EXPOSE 22  

