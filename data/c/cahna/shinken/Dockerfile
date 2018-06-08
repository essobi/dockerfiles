  
FROM ubuntu:15.04  
MAINTAINER Conor Heine <conor.heine@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_TYPE en_US.UTF-8  
# Core dependencies  
RUN locale-gen en_US.UTF-8  
RUN apt-get update  
RUN apt-get --yes install \  
lsb-release \  
wget \  
sudo \  
inotify-tools \  
libssl-dev \  
libsys-statistics-linux-perl \  
libapache2-mod-proxy-html \  
supervisor \  
ntp  
  
# Extra dependencies  
RUN apt-get --yes install \  
mongodb \  
nagios-plugins \  
nagios-nrpe-plugin  
  
# Python  
RUN apt-get --yes install \  
python2.7 \  
python-setuptools \  
python-pip \  
python-pycurl \  
python-cherrypy3 \  
python-pymongo \  
python-requests \  
python-arrow \  
python-openssl \  
python-bottle \  
python-crypto  
  
# Pip  
RUN pip install docker-py nagiosplugin pymongo>=3.0.3 requests arrow
bottle==0.12.8  
  
# Install shinken  
RUN useradd -U --system -m -d /var/lib/shinken shinken  
RUN echo 'shinken ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
RUN wget -O /tmp/shinken.tgz
https://github.com/naparuba/shinken/tarball/master  
RUN cd /tmp && tar zxvf shinken.tgz && cd nap* && python2.7 setup.py install  
RUN cd /tmp/nap* && contrib/install -a mongodb  
RUN shinken --init  
  
# Install mod-webui2  
RUN mkdir -p /var/lib/shinken/modules/webui2  
RUN wget -O /tmp/webui2.tgz https://github.com/shinken-monitoring/mod-
webui/tarball/master && cd /tmp && tar zxvf webui2.tgz && rm webui2.tgz  
RUN cd /tmp/shinken* && cp -R ./* /var/lib/shinken/modules/webui2/  
  
# permissions/filesystem cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mkdir -p /var/lib/shinken/config /var/lib/shinken/share/photos  
RUN chown -R shinken:shinken /var/lib/shinken /var/run/shinken
/var/log/shinken /etc/shinken  
  
VOLUME /etc/shinken  
VOLUME /var/log/shinken  
VOLUME /var/run/shinken  
  
# Be sure to configure root user/group and 'idontcareaboutsecurity=1'  
USER root  
WORKDIR /var/lib/shinken  
CMD shinken-arbiter -v -c /etc/shinken/shinken.cfg  
  

