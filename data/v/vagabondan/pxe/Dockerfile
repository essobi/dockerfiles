FROM ubuntu:xenial  
  
MAINTAINER Vagabondan <strannix.vagabondan@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
WORKDIR /app  
RUN apt-get -q -y update \  
&& apt-get -q -y -o "DPkg::Options::=--force-confold" -o
"DPkg::Options::=--force-confdef" install apt-utils \  
&& apt-get -q -y -o "DPkg::Options::=--force-confold" -o
"DPkg::Options::=--force-confdef" dist-upgrade \  
&& apt-get -q -y -o "DPkg::Options::=--force-confold" -o
"DPkg::Options::=--force-confdef" install isc-dhcp-server man \  
&& apt-get -q -y -o "DPkg::Options::=--force-confold" -o
"DPkg::Options::=--force-confdef" install wget git \  
&& apt-get -q -y -o "DPkg::Options::=--force-confold" -o
"DPkg::Options::=--force-confdef" install tftpd-hpa \  
&& apt-get -q -y -o "DPkg::Options::=--force-confold" -o
"DPkg::Options::=--force-confdef" install apache2 \  
&& apt-get -q -y autoremove \  
&& apt-get -q -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# using dumb-init instead of original init to orchestrate children  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 \  
&& chmod +x /usr/local/bin/dumb-init \  
&& git clone https://github.com/vagabondan/docker-pxe.git .  
  
# centos7  
# RUN mkdir -p /tftp/centos/7 \  
# &&wget -O /tftp/centos/7/initrd.img
http://mirror.centos.org/centos/7/os/x86_64/images/pxeboot/initrd.img \  
# && wget -O /tftp/centos/7/vmlinuz
http://mirror.centos.org/centos/7/os/x86_64/images/pxeboot/vmlinuz \  
# && chmod 444 /tftp/centos/7/*  
# get Ubuntu 1604 from network  
# RUN mkdir -p /tftp/ubuntu/1604 \  
# && wget http://archive.ubuntu.com/ubuntu/dists/xenial/main/installer-
amd64/current/images/netboot/ubuntu-installer/amd64/initrd.gz \  
# -O /tftp/ubuntu/1604/initrd.gz \  
# && wget http://archive.ubuntu.com/ubuntu/dists/xenial/main/installer-
amd64/current/images/netboot/ubuntu-installer/amd64/linux \  
# -O /tftp/ubuntu/1604/linux \  
# && chmod 444 /tftp/ubuntu/1604/*  
# get Ubuntu 1804 from network  
# RUN mkdir -p /tftp/ubuntu/1804 \  
# && wget http://archive.ubuntu.com/ubuntu/dists/bionic/main/installer-
amd64/current/images/netboot/ubuntu-installer/amd64/initrd.gz \  
# -O /tftp/ubuntu/1804/initrd.gz \  
# && wget http://archive.ubuntu.com/ubuntu/dists/bionic/main/installer-
amd64/current/images/netboot/ubuntu-installer/amd64/linux \  
# -O /tftp/ubuntu/1804/linux \  
# && chmod 444 /tftp/ubuntu/1804/*  
# For debug only. Delete on release  
# COPY . .  
# Release  
RUN mv ./tftp /tftp && mv ./dhcp /dhcp  
  
# For debug. Comment on release  
# VOLUME ["/dhcp","/tftp"]  
ENTRYPOINT ["/app/util/entrypoint.sh"]  

