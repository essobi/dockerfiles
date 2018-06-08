FROM ubuntu:trusty  
  
MAINTAINER Andrei Susanu <andrei.susanu@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# add MySQL official repository  
RUN echo "deb http://repo.mysql.com/apt/ubuntu/ `lsb_release -cs` mysql-5.6" >
/etc/apt/sources.list.d/mysql-server-5.6.list  
  
# set root password for MySQL before package install  
RUN echo mysql-community-server mysql-community-server/root-pass password '' |
debconf-set-selections  
RUN echo mysql-community-server mysql-community-server/re-root-pass password
'' | debconf-set-selections  
  
# update, upgrade and install new packages  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y --force-yes --no-install-recommends install \  
mysql-server-5.6 \  
mysql-client-5.6  
  
# MySQL config  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]"
&& c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
  
# grant privileges for root to any host  
RUN service mysql start && mysql -e 'GRANT ALL PRIVILEGES ON *.* TO "root"@"%"
WITH GRANT OPTION;'  
  
# clear apt cache and remove unnecessary packages  
RUN apt-get autoclean && apt-get -y autoremove  
  
# mountable directory for mysql databases  
VOLUME ["/var/lib/mysql"]  
  
# mysql  
EXPOSE 3306  
CMD ["/usr/sbin/mysqld"]  

