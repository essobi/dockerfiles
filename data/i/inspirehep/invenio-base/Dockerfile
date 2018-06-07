FROM ubuntu:14.10  
MAINTAINER Federico Poli "federico.poli@cern.ch"  
  
################  
# Requirements #  
################  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
mariadb-server libmariadbclient-dev redis-server \  
libssl-dev libxml2-dev libxslt-dev git unzip wget \  
gnuplot clisp automake pstotext gettext postfix \  
libhdf5-dev poppler-utils libapache2-mod-xsendfile \  
apache2-mpm-worker libapache2-mod-wsgi \  
python-dev python-pip  
  
# RUN pip install -q devpi-client  
# RUN devpi use http://inspireprovisioning.cern.ch/root/inspire --set-cfg  
  
ADD requirements.txt /home/drone/requirements.txt  
RUN sudo pip install -r /home/drone/requirements.txt  
  
#######################  
# Basic configuration #  
#######################  
  
RUN dpkg-reconfigure locales && \  
locale-gen en_US.UTF-8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
  
RUN mkdir -p /etc/apache2/ssl  
RUN /usr/sbin/a2dissite 000-default  
RUN /usr/sbin/a2enmod ssl  
RUN /usr/sbin/a2enmod xsendfile  

