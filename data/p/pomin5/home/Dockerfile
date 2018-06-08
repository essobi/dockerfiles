FROM debian:wheezy  
MAINTAINER Pomin Wu <pomin5@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV REFRESHED_AT 2014-12-08  
ENV DEVELOPER_USER developer  
ENV DEVELOPER_GROUP developer  
ENV DEVELOPER_HOME /home/developer  
ENV PASSWORD_FILE /home/developer/password.txt  
  
RUN apt-get update && \  
apt-get install -yq openssh-server sudo pwgen && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN mkdir /var/run/sshd # privilege separation directory required by sshd  
  
RUN groupadd -g 1000 ${DEVELOPER_GROUP} && \  
useradd -u 1000 -g ${DEVELOPER_GROUP} \--home-dir ${DEVELOPER_HOME} -m
${DEVELOPER_USER}  
  
VOLUME ["/home"]  
  
ADD init.sh /init.sh  
ADD run.sh /run.sh  
  
EXPOSE 22  
CMD ["/run.sh"]  

