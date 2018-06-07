FROM erickbrower/base:ubuntu_13.10  
RUN apt-get remove --purge -y mysql* && apt-get autoremove -y  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A  
  
RUN echo "deb http://repo.percona.com/apt saucy main" >> /etc/apt/sources.list  
RUN echo "deb-src http://repo.percona.com/apt saucy main" >>
/etc/apt/sources.list  
ADD ./00percona.pref /etc/apt/preferences.d/00percona.pref  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes percona-
server-server-5.6 percona-server-client-5.6  
RUN apt-get install -f -y  
  
ADD ./my.cnf /etc/mysql/my.cnf  
ADD ./set-access-rights.sh /tmp/set-access-rights.sh  
RUN /bin/sh /tmp/set-access-rights.sh  
  
EXPOSE 3306  
CMD ["/usr/sbin/mysqld", "--user=root"]  

