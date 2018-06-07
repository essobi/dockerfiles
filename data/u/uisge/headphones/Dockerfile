FROM phusion/baseimage:0.9.19  
MAINTAINER https://github.com/uisge-beatha  
ENV DEBIAN_FRONTEND noninteractive  
  
######################################  
## Environment  
######################################  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
######################################  
# Set correct environment variables  
######################################  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
######################################  
## Configure Directories  
######################################  
## SickRage configuration folder  
VOLUME /NZBGet-config  
  
## SickRage watched folder  
VOLUME /watched  
  
## Downloads  
VOLUME /downloads  
  
## SSL keys & certs  
VOLUME /certs  
  
## media  
VOLUME /media  
  
RUN mkdir -p /files /home/ashtaroth  
  
######################################  
## Upgrade OS  
######################################  
RUN apt-get update -q && apt-get upgrade -y -o Dpkg::Options::="--force-
confold"  
######################################  
## Misc setup  
######################################  
  
RUN add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu/ xenial
multiverse"  
RUN add-apt-repository -y "deb http://us.archive.ubuntu.com/ubuntu/ xenial-
updates multiverse"  
RUN apt-get update -qq  
  
#Install general utilities  
RUN apt-get install -qy python2.7 git-core avahi-daemon avahi-utils  
  
######################################  
## Python setup  
######################################  
RUN ln -s /usr/bin/python2.7 /usr/bin/python2  
RUN ln -s /usr/bin/python2.7 /usr/bin/python  
  
######################################  
## Avahi setup  
######################################  
#DBUS requires this directory  
RUN mkdir -p /var/run/dbus  
VOLUME /var/run/dbus  
  
#Configure Avahi  
ADD avahi-daemon.conf /etc/avahi/avahi-daemon.conf  
  
  
######################################  
## Headphones setup  
######################################  
  
RUN git clone https://github.com/rembo10/headphones.git /opt/headphones  
  
  
######################################  
## Expose Ports  
######################################  
## SickRage  
EXPOSE 30005  
######################################  
## Add Services to runit  
######################################  
## Add Headphones  
RUN mkdir /etc/service/Headphones  
ADD Headphones.sh /etc/service/Headphones/run  
RUN chmod +x /etc/service/Headphones/run  
  
  
  
######################################  
## Add boot scripts  
######################################  
# Add initd.sh to execute during container startup  
ADD initd.sh /etc/my_init.d/initd.sh  
RUN chmod +x /etc/my_init.d/initd.sh  
  
######################################  
## Clean up APT when done.  
######################################  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

