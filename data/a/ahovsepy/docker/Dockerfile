#Dockerfile for RHQ 4.9.0  
FROM mattdm/fedora  
  
MAINTAINER Armine Hovsepyan <ahovsepy@redhat.com>  
  
# install missing commands  
RUN yum -y update  
RUN yum -y install wget unzip vim expect spawn  
  
# Install java  
RUN yum -y install java-1.7.0-openjdk-devel  
  
# Install postgresql  
RUN yum -y install postgresql-server  
  
# Init postgres service  
RUN su -l postgres -c "/usr/bin/initdb --pgdata='/var/lib/pgsql/data'
--auth='ident'" \ >> "/var/lib/pgsql/initdb.log" 2>&1 < /dev/null  
  
# Edit postgres config  
RUN sed 's/ident/trust/' /var/lib/pgsql/data/pg_hba.conf > pg_hba.conf  
  
# Replace old properties file with the new one  
RUN cp -u pg_hba.conf /var/lib/pgsql/data/pg_hba.conf  
  
# Start postgres service, create rhqadmin role and rhq db  
RUN expect -c ' spawn su -l postgres -c " pg_ctl start " ; expect -re "pg_log"
{send \"\r\"; exp_continue } }';\  
ps -aux; expect -c ' spawn createuser -h 127.0.0.1 -p 5432 -U postgres -S -D
-R -P rhqadmin; expect -re "Enter" { send \"\r\"; exp_continue } "Enter" {
send \"\r\"; exp_continue } ';\  
createdb -h 127.0.0.1 -p 5432 -U postgres -O rhqadmin rhq;  
  
# Download rhq-server-4.10.0.zip from sourceforge  
RUN wget http://sourceforge.net/projects/rhq/files/rhq/rhq-4.10/rhq-
server-4.10.0.zip/download -O /opt/rhq-server-4.10.0.zip  
  
# Go to opt directory  
RUN cd /opt  
  
# Unzip rhq-server-4.10.0.zip  
RUN unzip /opt/rhq-server-4.10.0.zip -d /opt  
  
# Change jboss.bind.address  
RUN sed
's/rhq.server.management.password=/rhq.server.management.password=35c160c1f841a889d4cda53f0bfc94b6/;s/jboss.bind.address=/jboss.bind.address=0.0.0.0/;s/rhq.storage.nodes=/rhq.storage.nodes=127.0.0.1/'
/opt/rhq-server-4.10.0/bin/rhq-server.properties > rhq-server.properties  
  
# Replace old properties file with the new one  
RUN cp -u rhq-server.properties /opt/rhq-server-4.10.0/bin/rhq-
server.properties  
  
ENV RHQ_SERVER_JAVA_EXE_FILE_PATH /usr/bin/java  
  
EXPOSE 7080  
ENTRYPOINT expect -c ' spawn su -l postgres -c " pg_ctl start " ; expect -re
"pg_log" {send \"\r\"; exp_continue } }' ;\  
su root -c ' ./opt/rhq-server-4.10.0/bin/rhqctl install --start ';\  
su root -c 'tail -f /opt/rhq-server-4.10.0/logs/server.log';  
  
CMD []  

