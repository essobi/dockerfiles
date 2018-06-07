FROM debian:squeeze  
  
MAINTAINER Mark Stillwell <mark@stillwell.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed --in-place 's/main/main contrib non-free/' /etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install \  
curl \  
g++ \  
ganglia-monitor \  
gfortran \  
git \  
gmetad \  
less \  
libatlas-base-dev \  
libatlas3gf-base \  
libxslt1-dev \  
logtail \  
memcached \  
nginx \  
ntp \  
openssh-server \  
python \  
python-dev \  
python-cheetah \  
python-m2crypto \  
python-netaddr \  
python-openssl \  
python-pip \  
python-pycurl \  
python-scipy \  
python-setuptools \  
python-simplejson \  
rrdtool \  
runit \  
subversion \  
tomcat6-user \  
unzip \  
wget \  
yaws && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN easy_install numpy && \  
easy_install -U numpy && \  
easy_install pandas && \  
easy_install patsy && \  
easy_install statsmodels  
  
# MaxelerOS  
RUN apt-get update && \  
apt-get -y install \  
infiniband-diags \  
iptables \  
libgomp1 \  
libmlx4-1 \  
nano \  
net-tools \  
wget && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#XtreemFS  
#RUN wget -q
http://download.opensuse.org/repositories/home:/xtreemfs/xUbuntu_14.04/Release.key
-O - | sudo apt-key add -  
#RUN apt-add-repository "deb
http://download.opensuse.org/repositories/home:/xtreemfs/xUbuntu_14.04 ./"  
#RUN apt-get update && \  
# apt-get -y install xtreemfs-client && \  
# rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
# StartUp  
ADD ./setmaxorch.sh /usr/local/bin/setmaxorch.sh  
RUN chmod 0755 /usr/local/bin/setmaxorch.sh  
RUN >> /etc/bash.bashrc echo '\  
export LD_LIBRARY_PATH=/opt/maxeler/maxeleros/lib:$LD_LIBRARY_PATH\n\  
export SLIC_CONF="default_engine_resource=192.168.0.10 disable_pcc=true"\n\  
export PATH=/opt/maxeler/maxeleros/utils:$PATH\n'  
  
# create directory structure  
RUN echo > /var/log/cpsagent.log  
RUN mkdir -p /etc/cpsagent/  
RUN mkdir -p /var/tmp/cpsagent/  
RUN mkdir -p /var/run/cpsagent/  
RUN mkdir -p /var/cache/cpsagent/  
RUN echo > /var/log/cpsmanager.log  
RUN mkdir -p /etc/cpsmanager/  
RUN mkdir -p /var/tmp/cpsmanager/  
RUN mkdir -p /var/run/cpsmanager/  
RUN mkdir -p /var/cache/cpsmanager/  
  
ADD 998-ec2 /usr/local/bin/conpaas-ec2  
RUN chmod 0755 /usr/local/bin/conpaas-ec2  
  
RUN mkdir -p /etc/service/sshd && \  
echo '#!/bin/sh\nmkdir -p /var/run/sshd\nexec /usr/sbin/sshd -D' \  
> /etc/service/sshd/run && \  
chmod 0755 /etc/service/sshd/run  
  
EXPOSE 22  
VOLUME [ "/mnt/data/cccad3/jgfc", "/opt/maxeler" ]  
  
RUN echo "root:contrail" | chpasswd  
  
ADD start.sh /usr/local/bin/start.sh  
RUN chmod 0755 /usr/local/bin/start.sh  
  
CMD /usr/local/bin/start.sh  
  

