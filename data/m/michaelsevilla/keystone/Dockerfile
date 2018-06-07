FROM tutum/ubuntu:trusty  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
# install deps  
RUN echo "===> Installing keystone stuff..." && \  
apt-get update -y && \  
apt-get install -yq \  
python-pip \  
python-dev \  
keystone && \  
pip install \  
python-keystoneclient==1.7.1 \  
python-swiftclient && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* debian/  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 750 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

