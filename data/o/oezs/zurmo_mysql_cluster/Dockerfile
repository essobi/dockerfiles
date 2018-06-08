FROM ubuntu:14.04  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A  
RUN sed -i '/repo.percona.com/d' /etc/apt/sources.list  
RUN sh -c 'echo "deb http://repo.percona.com/apt precise main" >>
/etc/apt/sources.list'  
RUN sh -c 'echo "deb-src http://repo.percona.com/apt precise main" >>
/etc/apt/sources.list'  
RUN apt-get -q -y update  
RUN LC_ALL=en_US.utf8 DEBIAN_FRONTEND=noninteractive apt-get -o
Dpkg::Options::='--force-confnew' -qqy install nano wget psmisc libdbi-perl
libdbd-mysql-perl libwrap0 perl libaio1 mysql-client percona-xtrabackup
libssl0.9.8 libssl1.0.0 rsync netcat  
  
#RUN wget --no-check-certificate https://launchpad.net/codership-
mysql/5.5/5.5.34-25.9/+download/mysql-server-wsrep-5.5.34-25.9-amd64.deb  
RUN wget --no-check-certificate
http://releases.galeracluster.com/ubuntu/pool/main/m/mysql-wsrep-5.6/mysql-
wsrep-server-5.6_5.6.25-25.11-1trusty_amd64.deb  
  
#RUN wget --no-check-certificate
https://launchpad.net/galera/2.x/25.2.8/+download/galera-25.2.8-amd64.deb  
RUN wget --no-check-certificate
http://releases.galeracluster.com/ubuntu/pool/main/g/galera-3/galera-3_25.3.12-1trusty_amd64.deb  
#RUN dpkg -i galera-25.2.8-amd64.deb  
RUN dpkg -i galera-3_25.3.12-1trusty_amd64.deb  
  
#RUN dpkg -i mysql-server-wsrep-5.5.34-25.9-amd64.deb  
RUN dpkg -i mysql-wsrep-server-5.6_5.6.25-25.11-1trusty_amd64.deb  
  
RUN apt-get install -y vim  
RUN apt-get install -y nano  
ADD my.cnf /etc/mysql/my.cnf  
#ADD *.sql /  
ADD create_db.sql /  
ADD create_user.sql /  
ADD zurmo.sql /  
ADD setup_database.sh /  
RUN chmod +x /setup_database.sh  
  
VOLUME ["/etc/mysql", "/var/lib/mysql", "/var/log"]  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["mysqld_safe"]  
  
CMD /bin/bash /setup_database.sh  
  
# Expose ports.  
EXPOSE 3306 4444 4567 4568  

