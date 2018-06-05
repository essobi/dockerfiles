#Dockerfile for RHQ 4.11.0  
  
FROM fedora:20  
  
MAINTAINER Garik Khachikyan <gkhachik@redhat.com>  
  
ENV RHQ_VERSION 4.12.0  
  
# install missing commands  
RUN yum -y install wget unzip java-1.7.0-openjdk-devel postgresql-server  
  
# Init postgres service; Start postgres service, create rhqadmin role and rhq
db  
RUN \  
su -l postgres -c "/usr/bin/initdb --pgdata='/var/lib/pgsql/data'
--auth='ident'" \ >> "/var/lib/pgsql/initdb.log" 2>&1 < /dev/null;\  
sed -i 's/ident/trust/g' /var/lib/pgsql/data/pg_hba.conf;\  
su -l postgres -c " pg_ctl -l server.log -w stop; pg_ctl -l server.log -w
start; ";\  
createuser -h 127.0.0.1 -p 5432 -U postgres -S -D -R -w rhqadmin;\  
createdb -h 127.0.0.1 -p 5432 -U postgres -O rhqadmin rhq  
  
  
# Download rhq-server-${RHQ_VERSION}.zip from sourceforge; unzip & tune
jboss.bind.address  
RUN \  
wget -q http://sourceforge.net/projects/rhq/files/rhq/rhq-4.12/rhq-
server-${RHQ_VERSION}.zip -O /opt/rhq-server-${RHQ_VERSION}.zip 2>&1
>/dev/null;\  
unzip /opt/rhq-server-${RHQ_VERSION}.zip -d /opt 2>&1 >/dev/null;\  
sed -i
's/^rhq.server.management.password=.*/rhq.server.management.password=35c160c1f841a889d4cda53f0bfc94b6/g'
/opt/rhq-server-${RHQ_VERSION}/bin/rhq-server.properties;\  
sed -i 's/^jboss.bind.address=.*/jboss.bind.address=0.0.0.0/g' /opt/rhq-
server-${RHQ_VERSION}/bin/rhq-server.properties;\  
sed -i 's/^rhq.storage.nodes=.*/rhq.storage.nodes=127.0.0.1/g' /opt/rhq-
server-${RHQ_VERSION}/bin/rhq-server.properties  
  
ENV RHQ_SERVER_JAVA_EXE_FILE_PATH /usr/bin/java  
# Print out java version  
RUN \  
echo -e "\n** ** ** JAVA ** ** **\n";\  
java -version; ls -l /etc/alternatives/java; rpm -qa | grep openjdk;\  
echo -e "\n********************* \n"  
  
EXPOSE 7080  
  
ENTRYPOINT \  
su -l postgres -c " pg_ctl -l server.log -w stop; pg_ctl -l server.log -w
start; ";\  
su root -c '/opt/rhq-server-${RHQ_VERSION}/bin/rhqctl install \--agent-
preference="127.0.0.1" \--start \--agent \--server \--storage';\  
/bin/bash  

