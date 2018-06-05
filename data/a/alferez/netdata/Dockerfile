FROM debian:8  
MAINTAINER Jose A Alferez <correo@alferez.es>  
  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
#### Configure TimeZone  
RUN echo "Europe/Madrid" > /etc/timezone  
RUN dpkg-reconfigure tzdata  
  
#### Instalamos dependencias, Repositorios y Paquetes  
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get update -y --fix-missing  
RUN apt-get -y upgrade  
  
RUN apt-get install -y --fix-missing wget curl nano zip unzip zlib1g-dev uuid-
dev libmnl-dev gcc make git autoconf autogen automake pkg-config nodejs jq
mysql-client iw xmlstarlet nut-client squidclient  
  
WORKDIR /tmp  
ADD ./netdata /tmp/netdata  
WORKDIR /tmp/netdata  
RUN ./netdata-installer.sh  
  
WORKDIR /tmp  
RUN wget https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz  
RUN tar zxvf docker-latest.tgz  
RUN mv docker/docker /usr/sbin/  
RUN groupadd docker  
RUN gpasswd -a netdata docker  
RUN usermod -aG docker netdata  
  
EXPOSE 19999  
### Limpiamos  
RUN apt-get clean  
RUN rm -rf /tmp/* /var/tmp/*  
RUN rm -rf /var/lib/apt/lists/*  
  
### Personalizacion  
RUN echo "alias l='ls -la'" >> /root/.bashrc  
  
WORKDIR /  
  
CMD ["/usr/sbin/netdata", "-s", "/host", "-D"]  

