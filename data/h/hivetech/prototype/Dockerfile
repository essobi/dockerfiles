# hivetech/salt-minion image  
# A generic machine ready to be configured by salt-minion or ansible  
# inspired from https://github.com/toscanini/docker-salt-
minion/blob/master/Dockerfile  
# VERSION 0.0.1  
# Administration  
FROM boxcar/raring  
MAINTAINER Xavier Bruhiere, xavier.bruhiere@gmail.com  
  
# Make sure the package repository is up to date  
RUN echo "deb http://archive.ubuntu.com/ubuntu raring main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Local settings  
# Change eventually fr_FR to us_US  
RUN apt-get install -y language-pack-fr  
ENV LANGUAGE fr_FR.UTF-8  
ENV LANG fr_FR.UTF-8  
ENV LC_ALL fr_FR.UTF-8  
RUN locale-gen fr_FR.UTF-8  
RUN dpkg-reconfigure locales  
  
# Common needed stuff for an efficient ansible-ready machine  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python python-apt \  
python-pip build-essential gcc python-dev wget sudo git-core python-software-
properties  
  
# Create a normal default user (vagrant / docker images have just vagrant /
root)  
# #TODO I'm pretty sure there is a smarter way to do that  
RUN useradd -m -d /home/prototype -g 100 -s /bin/bash prototype  
RUN echo "prototype:proto" | chpasswd && \  
adduser prototype sudo && \  
groupadd prototype && \  
adduser prototype prototype  
  
#Supervisord  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor && \  
mkdir -p /var/log/supervisor  
  
RUN apt-get install -y python-software-properties  
RUN add-apt-repository ppa:saltstack/salt  
RUN apt-get update  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -s /bin/true /sbin/initctl  
  
RUN apt-get install -y salt-minion  
  
ADD ./startup /usr/bin/startup  
ADD ./supervisor-salt.conf /etc/supervisord.conf  
  
#SSHD  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server && \  
echo 'root:proto' | chpasswd  
RUN test -d /var/run/sshd || mkdir /var/run/sshd  
  
ENTRYPOINT ["/usr/bin/supervisord", "-n"]  
  
EXPOSE 22 8080  

