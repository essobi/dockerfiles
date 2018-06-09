FROM debian:stable  
MAINTAINER Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN ["/usr/sbin/adduser", "--system", "--shell", "/bin/bash", "--gecos", \  
"Backup and Recovery Manager for PostgreSQL", "--home", \  
"/home/pg-backup", "--group", "--disabled-password", "pg-backup"]  
RUN apt-get -q -y update && apt-get -q -y -o Dpkg::Options::=--force-confdef \  
-o Dpkg::Options::=--force-confold --purge install postgresql-client-9.6 \  
autopostgresqlbackup ssmtp bsd-mailx coreutils  
  
COPY launcher.sh /usr/local/bin/launcher.sh  
RUN ["/bin/chmod", "a+x", "/usr/local/bin/launcher.sh"]  
  
VOLUME ["/backup", "/etc/ssmtp"]  
  
ENTRYPOINT ["/usr/local/bin/launcher.sh"]  

