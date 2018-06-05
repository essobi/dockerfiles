###############################################################################  
# Name: Dockerfile  
# Author: Daniel Middleton <daniel-middleton.com>  
# Description: Dockerfile used to build dannydirect/blesta  
# Usage: docker build -t dannydirect/blesta:latest .  
################################################################################  
  
FROM phusion/baseimage:latest  
  
MAINTAINER Daniel Middleton <daniel-middleton.com>  
  
# Add entrypoint script  
#ADD run.py /opt/docker-blesta/run.py  
  
# Install Updates, Python3, Pip3, LAMP, Unzip, Wget  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && apt-get -y upgrade && \  
apt-get -y install python3 && \  
ln -s /usr/bin/python3 /usr/bin/python && \  
apt-get -y install python3-pip && \  
ln -s /usr/bin/pip3 /usr/bin/pip && \  
pip install pycurl && \  
apt-get -y install lamp-server^ && \  
apt-get -y install unzip && \  
apt-get -y install wget  
  
# Download and Extract the latest Blesta archive  
# TODO: Automate getting latest version  
RUN wget -P /tmp
https://account.blesta.com/client/plugin/download_manager/client_main/download/50/blesta-3.3.0.zip
&& \  
unzip /tmp/blesta-3.3.0.zip -d /tmp/blesta-extracted && \  
rm /var/www/html/index.html && \  
cp -r -v /tmp/blesta-extracted/blesta/* /var/www/html && \  
rm -rf /tmp/* && \  
echo && \  
echo '############# DEBUG #############' && \  
echo && \  
ls -la /var/www/html && \  
echo && \  
echo '#################################' && \  
echo  
  
RUN cd /var/www/html && \  
wget
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
&& \  
tar xvfz ioncube_loaders_lin_x86-64.tar.gz && \  
cd -  
  
RUN cp /var/www/html/ioncube/ioncube_loader_lin_5.5.so /usr/lib/php5/20121212  
  
RUN wget -P /tmp
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
&& \  
tar zxf /tmp/ioncube_loaders_lin_x86-64.tar.gz -C /usr/lib/php5/20121212  
  
RUN touch /etc/php5/apache2/conf.d/20-ioncube.ini && \  
echo 'zend_extension = /usr/lib/php5/20121212/ioncube_loader_lin_5.5.so' >
/etc/php5/apache2/conf.d/20-ioncube.ini  
  
#RUN sed -i "s,^Allow 127.0.0.1,$1," /etc/apache2/apache2.conf  
  
# Ports  
EXPOSE 80  
  
# Over to run.py  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

