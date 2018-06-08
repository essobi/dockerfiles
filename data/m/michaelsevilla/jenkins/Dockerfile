FROM jenkins  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
USER root  
ENV DEBIAN_FRONTEND=noninteractive  
RUN echo "===> Install Ansible..." && \  
apt-get update && \  
apt-get install -yq --force-yes vim software-properties-common && \  
echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" | tee
/etc/apt/sources.list.d/ansible.list && \  
echo "deb-src http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/ansible.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys 7BB9C367 &&
\  
apt-get update && \  
apt-get install -yq --force-yes ansible=2.0.2.0* apache2 php5 && \  
apt-get clean && rm -rf \  
/var/lib/apt/lists/* /etc/apt/sources.list.d/ansible.list \  
tmp/* /var/tmp/*  
  
COPY /httpd/ports.conf /etc/apache2/  
COPY /html /var/www/html  
  
RUN echo "===> Setup Apache to serve server statuses..." && \  
rm /var/www/html/index.html && \  
chmod 777 -R /var/www/html && \  
ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && \  
dpkg-reconfigure tzdata  

