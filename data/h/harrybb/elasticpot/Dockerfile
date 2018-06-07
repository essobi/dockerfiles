# ElasticPotPY Dockerfile by MO & MS  
#  
# VERSION 16.10  
FROM debian:jessie-slim  
MAINTAINER MS  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Include dist  
ADD dist/ /root/dist/  
# Setup apt  
RUN ln -snf /bin/bash /bin/sh && \  
apt-get update -y && \  
apt-get upgrade -y && \  
  
# Install packages  
apt-get install -y nano python python-setuptools supervisor git && \  
easy_install bottle requests configparser datetime && \  
cd /opt/ && git clone https://github.com/schmalle/ElasticpotPY.git && \  
  
# Setup user, groups and configs  
addgroup \--gid 2000 tpot && \  
adduser \--system \--no-create-home \--shell /bin/bash \--uid 2000
\--disabled-password \--disabled-login \--gid 2000 tpot && \  
mv /root/dist/supervisord.conf /etc/supervisor/conf.d/ && \  
  
# Clean up  
rm -rf /root/* && \  
apt-get purge git -y && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Start elasticpot  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  

