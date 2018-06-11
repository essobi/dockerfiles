FROM ubuntu:trusty  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -nfs /bin/true /sbin/initctl  
  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0xcbcb082a1bb943db && \  
echo "deb http://mariadb.mirror.iweb.com/repo/10.0/ubuntu `lsb_release -cs`
main" > /etc/apt/sources.list.d/mariadb.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
ADD ./startup.sh /opt/startup.sh  
  
VOLUME ["/var/lib/mysql"]  
EXPOSE 3306  
CMD ["/bin/bash", "/opt/startup.sh"]  

