FROM pataquets/ubuntu:trusty  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install python-setuptools \  
&& \  
easy_install supervisor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD ./etc/supervisor/ /etc/supervisor/  
  
RUN \  
mkdir -vp /etc/supervisor/conf.d ; \  
mkdir -vp /var/log/supervisor ; \  
mkdir -vp /var/run/supervisor  
  
EXPOSE 9001  

