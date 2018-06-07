#  
# ementux/mariadb  
#  
# MariaDB container and Serf for scalable web  
#  
# See https://github.com/ementux/docker  
#  
FROM ementux/base  
MAINTAINER Michal Grna <michal.grna@ementux.org>  
  
# install MariaDB  
RUN yum -y update && yum -y install mariadb mariadb-server pwgen unzip && yum
clean all  
  
# add configuration and wrapper for MariaDB  
COPY my.cnf /etc/my.cnf  
RUN chmod 644 /etc/my.cnf  
COPY config-mariadb.sh /config-mariadb.sh  
RUN chmod 755 /config-mariadb.sh  
RUN mkdir -p /etc/service/mariadb/  
COPY mariadb.run /etc/service/mariadb/run  
RUN chmod 755 /etc/service/mariadb/run  
  
# install Serf  
ADD https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip /tmp/serf.zip  
RUN unzip /tmp/serf.zip -d /usr/local/bin/  
RUN rm /tmp/serf.zip  
  
# add configuration files and handlers for Serf  
COPY serf-config /etc/serf  
RUN mkdir -p /etc/service/serf/  
COPY serf.run /etc/service/serf/run  
RUN chmod 755 /etc/service/serf/run  
  
# add volume for MariDB  
VOLUME [ "/var/lib/mysql" ]  
  
# expose MariaDB & Serf ports  
EXPOSE 3306 7946 7373  
# start MariaDB and Serf  
ENTRYPOINT [ "/usr/sbin/runit_bootstrap" ]  
  

