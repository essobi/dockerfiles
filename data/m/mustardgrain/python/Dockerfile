FROM mustardgrain/base:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
RUN \  
apt-get update ; \  
apt-get install -y python-dev python-setuptools ; \  
easy_install pip  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

