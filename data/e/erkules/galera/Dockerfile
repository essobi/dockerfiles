FROM ubuntu:16.04  
MAINTAINER erkan yanar <erkan.yanar@linsenraum.de>  
ENV VERSION 20170605  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 BC19DDBA &&
\  
add-apt-repository 'deb http://releases.galeracluster.com/ubuntu xenial main'
&& \  
apt-get update && \  
apt-get install -y galera-3 galera-arbitrator-3 mysql-wsrep-5.6 rsync lsof  
RUN rm -r /var/lib/mysql  
  
COPY my.cnf /etc/mysql/my.cnf  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 700 /entrypoint.sh  
EXPOSE 3306/tcp  
ENTRYPOINT ["/entrypoint.sh"]  
  
LABEL mysql_verion=5.6.35  
  

