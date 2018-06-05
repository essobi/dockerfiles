FROM phusion/baseimage:0.9.17  
MAINTAINER Morton Jonuschat <m.jonuschat@mojocode.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get -qy --no-install-recommends --fix-missing --force-yes install wget
strace lsof netcat software-properties-common && \  
update-locale LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8 && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
sh -c 'echo "deb http://ftp.hosteurope.de/mirror/mariadb.org/repo/10.1/ubuntu
trusty main" >> /etc/apt/sources.list.d/mariadb.list' && \  
apt-get update && \  
apt-get install -yq mariadb-server=10.1.8+maria-1~trusty mariadb-
client=10.1.8+maria-1~trusty mariadb-common=10.1.8+maria-1~trusty && \  
apt-get clean && \  
apt-get autoremove -y  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Startup jobs  
RUN mkdir -p /etc/my_init.d  
ADD my_init.d /etc/my_init.d  
  
# Service: mariadb  
RUN mkdir -p /etc/service/mariadb/log/main  
ADD configs/my.cnf /etc/mysql/my.cnf  
ADD runit/mariadb /etc/service/mariadb/run  
ADD runit/log /etc/service/mariadb/log/run  

