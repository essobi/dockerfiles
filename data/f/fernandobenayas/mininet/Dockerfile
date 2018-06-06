# Mininet  
FROM ubuntu:16.04  
MAINTAINER Fernando Benayas <ferbenayas94@gmail.com>  
#Based on the Dockerfile provided by Iwase Yusuke
(https://hub.docker.com/r/iwaseyusuke/mininet)  
USER root  
WORKDIR /root  
  
COPY entrypoint.sh /  
COPY mininet .  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl \  
sudo \  
iproute2 \  
# linux-headers-`uname -r` \  
iputils-ping \  
net-tools \  
socat \  
tcpdump \  
python \  
python-pip \  
python-setuptools \  
python-matplotlib \  
vim \  
vlc \  
x11-xserver-utils \  
xterm \  
git-all \  
lsb-release \  
&& rm -rf /var/lib/apt/lists/* \  
&& mv /bin/ping /sbin/ping \  
&& mv /bin/ping6 /sbin/ping6 \  
&& mv /usr/sbin/tcpdump /usr/bin/tcpdump \  
&& chmod +x /entrypoint.sh \  
&& chmod -R +x ./net \  
&& pip install -I networkx==1.11 \  
&& pip install matplotlib  
  
#RUN ln -s /usr/src/linux-headers-`uname -r`/ /lib/modules/`uname -r`/build  
RUN git config --global url.https://github.com/.insteadOf git://github.com/  
RUN git clone https://github.com/mininet/mininet  
WORKDIR /root/mininet  
RUN git checkout -b 2.2.2 2.2.2  
WORKDIR /root  
RUN chmod +x mininet/util/install.sh  
RUN mininet/util/install.sh -a  
  
# This part is optional: updating openvswitch  
#RUN apt-get -y remove openvswitch-common openvswitch-pki openvswitch-switch  
#WORKDIR /tmp  
#RUN wget http://openvswitch.org/releases/openvswitch-2.8.1.tar.gz \  
# && tar zxvf openvswitch-2.8.1.tar.gz  
#WORKDIR /tmp/openvswitch-2.8.1  
#RUN ./configure --prefix=/usr --with-linux=/lib/modules/`uname -r`/build \  
# && make \  
# && make install \  
# && make modules_install  
# End  
WORKDIR /root  
RUN curl -L -O
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.4.1-amd64.deb  
RUN dpkg -i filebeat-5.4.1-amd64.deb  
COPY filebeat.yml /etc/filebeat/  
RUN mkdir ./log/  
RUN chmod 644 /etc/filebeat/filebeat.yml  
  
RUN pip install --upgrade pip==9.0.1  
RUN pip install -U pip setuptools  
EXPOSE 6640  
ENTRYPOINT ["/entrypoint.sh"]  

