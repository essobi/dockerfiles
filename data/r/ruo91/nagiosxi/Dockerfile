#  
# Title: Dockerfile for Nagios XI  
#  
# Maintainer: Yongbok Kim (ruo91@yongbok.net)  
#  
# - Build  
# docker build --rm -t nagios:xi .  
#  
# - Run  
# docker run -d --name="nagiosxi" -h "nagiosxi" -p 80:80 -p 443:443 -p
5666:5666 -p 5667:5667 nagios:xi  
# Base images  
FROM centos:centos6  
MAINTAINER Yongbok Kim <ruo91@yongbok.net>  
  
# WorkDIR  
ENV SRC_DIR /opt  
WORKDIR $SRC_DIR  
  
# Nagios XI  
RUN curl -LO "http://assets.nagios.com/downloads/nagiosxi/xi-latest.tar.gz" \  
&& tar xzvf xi-latest.tar.gz  
  
# Disable firewall  
RUN cd nagiosxi \  
&& touch installed.firewall  
  
# Disable kernel parameter  
ADD conf/post-install.patch $SRC_DIR/nagiosxi/post-install.patch  
RUN yum install -y patch \  
&& cd nagiosxi \  
&& patch -p0 < post-install.patch  
  
# Build  
RUN cd nagiosxi \  
&& ./fullinstall -n  
  
# Supervisor  
RUN yum install -y python-setuptools python-meld3 \  
&& easy_install pip \  
&& pip install --upgrade pip \  
&& pip install supervisor \  
&& mkdir /etc/supervisord.d  
ADD conf/supervisord.conf /etc/supervisord.d/supervisord.conf  
  
# Ports  
EXPOSE 80 443 5666 5667  
# Supervisor  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.d/supervisord.conf"]  

