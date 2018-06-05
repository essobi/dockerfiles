#Dockerfile for RHQ 4.12.0  
FROM mattdm/fedora  
  
MAINTAINER Armine Hovsepyan <ahovsepy@redhat.com>  
  
  
# install missing commands  
RUN yum -y update  
RUN yum -y install wget unzip vim expect spawn  
  
# Install java  
RUN yum -y install java-1.7.0-openjdk-devel  
  
# Install and onfigure postgresql, create rhq database  
RUN yum -y install postgresql-server  
RUN su -l postgres -c "/usr/bin/initdb --pgdata='/var/lib/pgsql/data'
--auth='ident'" \ >> "/var/lib/pgsql/initdb.log" 2>&1 < /dev/null;\  
sed -i 's/ident/trust/g' /var/lib/pgsql/data/pg_hba.conf;\  
su -l postgres -c " pg_ctl -l server.log -w stop; pg_ctl -l server.log -w
start; ";\  
createuser -h 127.0.0.1 -p 5432 -U postgres -S -D -R -w rhqadmin;\  
createdb -h 127.0.0.1 -p 5432 -U postgres -O rhqadmin rhq  
  
# Download rhq-server-4.12.0.zip from sourceforge  
RUN wget http://sourceforge.net/projects/rhq/files/rhq/rhq-4.12/rhq-
server-4.12.0.zip/download -O /opt/rhq-server-4.12.0.zip  
  
# Go to opt directory  
RUN cd /opt  
  
# Unzip rhq-server-4.12.0.zip  
RUN unzip /opt/rhq-server-4.12.0.zip -d /opt  
  
# Change jboss.bind.address  
RUN sed -i
's/^rhq.server.management.password=.*/rhq.server.management.password=35c160c1f841a889d4cda53f0bfc94b6/g'
/opt/rhq-server-4.12.0/bin/rhq-server.properties;\  
sed -i 's/^jboss.bind.address=.*/jboss.bind.address=0.0.0.0/g' /opt/rhq-
server-4.12.0/bin/rhq-server.properties;\  
sed -i 's/^rhq.storage.nodes=.*/rhq.storage.nodes=127.0.0.1/g' /opt/rhq-
server-4.12.0/bin/rhq-server.properties  
  
ENV RHQ_SERVER_JAVA_EXE_FILE_PATH /usr/bin/java  
  
EXPOSE 7080  
ADD startRHQ.sh /usr/local/bin/startRHQ.sh  
  
RUN chmod +x /usr/local/bin/startRHQ.sh  
  
ENTRYPOINT su root -c './usr/local/bin/startRHQ.sh'  
  
CMD []  

