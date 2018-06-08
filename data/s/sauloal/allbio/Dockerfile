# VERSION 0.1  
# DOCKER-VERSION 0.10.0  
# AUTHOR Saulo Alves <sauloal@gmail.com>  
# DESCRIPTION  
# TO BUILD docker build -t sauloal/allbio .  
FROM sauloal/supervisor  
  
MAINTAINER Saulo Alves <sauloal@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
  
RUN dpkg --add-architecture i386; \  
apt-get update; \  
apt-get install -f -y unzip git curl htop wget subversion \  
build-essential mercurial autoconf automake subversion libtool \  
unzip curl htop wget nano  
  
RUN apt-get install -y time python-pip \  
python-dev python-numpy python-scipy python-matplotlib ipython \  
ipython-notebook python-pandas python-sympy python-nose \  
libboost-all-dev python-biopython  
  
RUN apt-get install -y libatlas-base-dev gfortran ant default-jdk \  
libboost-all-dev libgd2-xpm-dev libncurses5-dev dialog cmake  
  
ADD postinstall.sh /root/postinstall.sh  
ADD firstboot.sh /root/firstboot.sh  
ADD mountall.sh /root/mountall.sh  
  
RUN /bin/bash /root/postinstall.sh  
RUN /bin/bash /root/firstboot.sh  
  
VOLUME /opt/allbio/data  
  

