FROM ubuntu:xenial  
MAINTAINER Diego Tiscornia <diegobt@gmail.com>  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV TINI_VERSION v0.13.0  
RUN apt-get update && apt-get install apt-utils -y  
  
#Install required packages  
RUN apt-get install python python-pip python-dev libffi-dev libssl-dev tcpdump
libssl-dev libxml2-dev libxslt1-dev python-dev libjpeg-dev wget gosu golang
libpciaccess-dev libnl-3-dev pkg-config libxml2-dev libgnutls-dev
libdevmapper-dev libcurl4-gnutls-dev libnl-route-3-dev python-libvirt sshpass
net-tools iputils-ping -y  
  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump \  
&& useradd cuckoo \  
&& wget http://libvirt.org/sources/libvirt-1.3.4.tar.gz \  
&& tar zxf libvirt-1.3.4.tar.gz \  
&& cd libvirt-1.3.4 \  
&& ./configure --with-esx=yes \  
&& make \  
&& make install  
  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/sbin/tini  
RUN chmod +x /sbin/tini  
  
WORKDIR /home/cuckoo  
ADD http://downloads.cuckoosandbox.org/cuckoo-current.tar.gz /home/cuckoo/  
RUN tar xvf cuckoo-current.tar.gz \  
&& chown -R cuckoo:cuckoo /home/cuckoo/cuckoo  
  
COPY requirements.txt /home/cuckoo/cuckoo/  
  
WORKDIR /home/cuckoo/cuckoo  
RUN pip install --upgrade pip \  
&& pip install -r requirements.txt \  
&& utils/community.py -wafb monitor  
  
COPY conf/* /home/cuckoo/cuckoo/conf/  
COPY entrypoint.sh /home/cuckoo/cuckoo/  
COPY scripts/VBoxManage /sbin/VBoxManage  
COPY example/pafish.exe /home/cuckoo/cuckoo/  
  
ENTRYPOINT ["/home/cuckoo/cuckoo/entrypoint.sh"]  

