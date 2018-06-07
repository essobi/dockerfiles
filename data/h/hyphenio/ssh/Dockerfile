FROM ubuntu:16.04  
MAINTAINER Hyphen IO <services@hyphenio.com.au>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
locale-gen en_US.UTF-8  
  
RUN apt-get install -y \  
curl \  
git \  
htop \  
man \  
software-properties-common \  
unzip \  
vim \  
wget \  
openssh-server  
  
RUN apt-get clean && apt-get autoclean && apt-get -y autoremove  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV HOME /root  
  
RUN apt-get -y install supervisor && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
RUN mkdir -p /root/.ssh && \  
chmod 600 /root/.ssh  
  
RUN mkdir -p /var/run/sshd && \  
chmod 755 /var/run/sshd  
  
ADD deployment /root/.ssh/deployment  
ADD gitwrapper.sh /root/.ssh/gitwrapper.sh  
ADD id_ssh.pub /root/.ssh/authorized_keys  
ADD supervisor.conf /etc/supervisor/supervisord.conf  
ADD sshd.conf /etc/supervisor/conf.d/sshd.conf  
ADD deploy.sh /bin/deploy.sh  
RUN chmod 600 /root/.ssh/deployment  
RUN chmod 700 /root/.ssh/gitwrapper.sh  
RUN chmod 600 /root/.ssh/authorized_keys  
  
EXPOSE 22  
CMD ["/bin/deploy.sh"]  

