FROM pmetpublic/baseimage:0.9.18  
MAINTAINER Keith Bentrup <kbentrup@magento.com>  
  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository 'deb
http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.1/ubuntu trusty main' &&
\  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes mariadb-server \  
pv && \  
apt-get --purge autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
COPY conf/additional.cnf /etc/mysql/conf.d/  
COPY mysql.sh /etc/service/mysql/run  
COPY db-startup.sh /etc/my_init.d/01_db-startup.sh  
  
EXPOSE 3306  

