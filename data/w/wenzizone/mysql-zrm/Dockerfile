# Mysql  
#  
FROM wenzizone/base  
MAINTAINER wenzizone <wenzizone@126.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install mysql server  
RUN apt-get update && \  
apt-get install -y curl libxml-parser-perl libdbd-mysql-perl mysql-server && \  
apt-get clean  
  
#install Percona XtraBackup  
ENV XTRABACKUP_VERSION 2.3.2  
RUN set -x; \  
curl -o percona-xtrabackup.deb -SL
https://www.percona.com/downloads/XtraBackup/Percona-
XtraBackup-${XTRABACKUP_VERSION}/binary/debian/trusty/x86_64/percona-
xtrabackup_${XTRABACKUP_VERSION}-1.trusty_amd64.deb \  
&& dpkg --force-depends -i percona-xtrabackup.deb \  
&& apt-get update \  
&& apt-get -y install -f --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* percona-xtrabackup.deb  
  
# install mysql zrm  
ENV ZRM_VERSION 3.0.0  
ENV ZRM_MAIN_VERSION 3.0  
RUN set -x; \  
curl -o mysql-zrm.deb -SL http://zmanda.com/downloads/community/ZRM-
MySQL/${ZRM_MAIN_VERSION}/Debian/mysql-zrm_${ZRM_VERSION}_all.deb \  
&& dpkg --force-depends -i mysql-zrm.deb \  
&& apt-get update \  
&& apt-get -y install -f --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* mysql-zrm.deb  
  
ADD my.cnf /etc/mysql/my.cnf  
#RUN sed -i "s/bind/#bind/" /etc/mysql/my.cnf  
ADD mysql-zrm.conf /etc/mysql-zrm/mysql-zrm.conf  
  
ADD launch.bash /launch  
RUN chmod +x /launch  
  
VOLUME ["/var/lib/mysql", "/var/lib/mysql-zrm"]  
  
CMD ["/launch"]

