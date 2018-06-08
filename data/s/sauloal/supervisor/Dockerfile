#BUILD docker build -t sauloal/supervisor .  
#  
#  
#https://github.com/Krijger/docker-cookbooks/blob/master/supervisor/Dockerfile  
#http://blog.trifork.com/2014/03/11/using-supervisor-with-docker-to-manage-
processes-supporting-image-inheritance/  
FROM ubuntu:14.04  
MAINTAINER Quinten Krijger "https://github.com/Krijger"  
ENV DEBIAN_FRONTEND noninteractive  
  
# make sure the package repository is up to date and update ubuntu  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
locale-gen en_US.UTF-8  
  
RUN apt-get install -y curl git htop man software-properties-common unzip vim
wget openssh-client openssh-server; \  
apt-get install -y libfuse2; \  
apt-get install -y fuse; \  
apt-get install -y sshfs  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV HOME /root  
  
# supervisor installation &&  
# create directory for child images to store configuration in  
RUN apt-get -y install supervisor && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
RUN mkdir /var/run/sshd; \  
mkdir /root/.ssh; \  
echo 'root:root' |chpasswd; \  
rm /dev/ptmx; \  
ln -s /dev/pts/ptmx /dev/ptmx; \  
sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config; \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# supervisor base configuration  
ADD supervisor.conf /etc/supervisor.conf  
ADD sshd.service.conf /etc/supervisor/conf.d/sshd.service.conf  
  
# default command  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

