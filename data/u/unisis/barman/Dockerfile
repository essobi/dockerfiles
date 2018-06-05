##################################################  
#  
# Dockerfile for BarMan  
#  
###################################################  
  
# Based on https://github.com/damiansoriano/barman-docker  
  
FROM unisis/base  
MAINTAINER Unisis <contacto@unisis.com.ar>  
  
# Expose port 22 (ssh)  
EXPOSE 22  
  
# /var/lib/barman is used to store the backups locally  
# PgBarman use SSH to backup from PostgreSQL, and we also  
# use SSH (rsync) to backup Odoo files in the post-x.sh scripts  
VOLUME [ "/var/lib/barman", "/var/log/barman" ]  
  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get -y install postgresql-client  
RUN apt-get -y install python  
RUN apt-get -y install python-pip  
RUN apt-get -y install postgresql-server-dev-all  
RUN apt-get -y install libpq-dev python-dev  
  
RUN pip install argcomplete  
RUN pip install argh  
RUN pip install psycopg2  
RUN pip install python-dateutil  
RUN pip install distribute  
  
RUN apt-get -y install barman  
RUN apt-get -y install man  
  
# From http://stackoverflow.com/questions/18173889/cannot-access-centos-sshd-
on-docker  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
# Copy config files  
ENV REFRESHED_AT 2016_05_15  
ADD config/ssh_config /root/ssh_config  
ADD config/barman.conf /root/barman.conf  
  
# Install script to be executed by barman after full backup  
ADD scripts/post-backup.sh /usr/bin/post-backup.sh  
RUN chmod a+x /usr/bin/post-backup.sh  
  
# Install script to be executed by barman after WAL archiving  
ADD scripts/post-archive.sh /usr/bin/post-archive.sh  
RUN chmod a+x /usr/bin/post-archive.sh  
  
# Install script to trigger a restore  
ADD scripts/restore-backup.sh /usr/bin/restore-backup.sh  
RUN chmod a+x /usr/bin/restore-backup.sh  
  
# Install startup script  
ADD scripts/start.sh /root/start.sh  
RUN chmod u+x /root/start.sh  
  
# Install init script  
ADD scripts/init.sh /root/init.sh  
RUN chmod u+x /root/init.sh  
  
# Run Init script  
CMD ["/root/start.sh"]  

