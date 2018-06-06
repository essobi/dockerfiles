# Dockerfile for the PDC's Endpoint collection of services  
#  
#  
# Converts SQL to deidentified to E2E, which is queried as aggregate data.  
# Requires pre-configured and pre-approved SSH keys. Contact admin@pdcbc.ca.  
#  
# Example:  
# sudo docker pull pdcbc/endpoint  
# sudo docker run -d --name=gateway --restart=always \  
# -v /encrypted/volumes/:/volumes/  
# -e GATEWAY_ID=9999 \  
# -e DOCTOR_IDS=11111,22222,...,99999  
# pdcbc/endpoint  
#  
#  
FROM phusion/passenger-ruby19  
MAINTAINER derek.roberts@gmail.com  
  
  
# Release numbers  
#  
ENV GATEWAY_REL 0.1.5  
ENV MONGO_MAJOR 3.2  
ENV MONGO_VERSION 3.2.0  
################################################################################  
# System and packages  
################################################################################  
# Update system and packages  
#  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' \  
>> /etc/apt/sources.list.d/webupd8team-java-trusty.list; \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886; \  
echo oracle-java6-installer shared/accepted-oracle-license-v1-1 \  
select true | /usr/bin/debconf-set-selections; \  
apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
42F3E95A2C4F08279C4960ADD68FA50FEA312927; \  
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/$MONGO_MAJOR
multiverse" > /etc/apt/sources.list.d/mongodb-org.list; \  
apt-get update; \  
apt-get install --no-install-recommends -y \  
autossh \  
ca-certificates \  
git \  
libmysql-java \  
mongodb-org=$MONGO_VERSION \  
mongodb-org-server=$MONGO_VERSION \  
mongodb-org-shell=$MONGO_VERSION \  
mongodb-org-mongos=$MONGO_VERSION \  
mongodb-org-tools=$MONGO_VERSION \  
mysql-server \  
numactl \  
oracle-java6-installer \  
tomcat6; \  
apt-get autoclean; \  
apt-get clean; \  
rm -rf \  
/etc/mongod.conf \  
/var/tmp/* \  
/var/lib/apt/lists/* \  
/var/lib/mongodb \  
/tmp/* \  
/usr/share/doc/ \  
/usr/share/doc-base/ \  
/usr/share/man/  
  
# Configure Tomcat6  
#  
ENV JAVA_HOME="/usr/lib/jvm/java-6-oracle"  
ENV CATALINA_HOME="/usr/share/tomcat6"  
ENV CATALINA_BASE="/var/lib/tomcat6"  
#  
RUN mkdir -p \  
${CATALINA_HOME}/server/classes/ \  
${CATALINA_HOME}/shared/classes/  
  
################################################################################  
# Users and groups  
################################################################################  
# AutoSSH user  
#  
RUN USER=autossh; \  
adduser --disabled-password --gecos '' \--home /home/${USER} ${USER}; \  
chown -R ${USER}:${USER} /home/${USER}  
  
################################################################################  
# Setup  
################################################################################  
# Prepare /gateway/ folder  
#  
WORKDIR /gateway/  
RUN git clone https://github.com/pdcbc/gateway.git . -b ${GATEWAY_REL}; \  
mkdir -p ./tmp/pids ./util/files; \  
gem install multipart-post; \  
chown -R app:app /gateway/; \  
/sbin/setuser app bundle install --path vendor/bundle  
  
# OSCAR 12 WebARchive (.war) and properties  
#  
COPY ./oscar/oscar12.properties /usr/share/tomcat6/  
WORKDIR ${CATALINA_BASE}/webapps/  
COPY ./oscar/oscar12.war.* ./  
RUN cat oscar12.war.* > oscar12.war; \  
rm oscar12.war.*  
  
# Start MySQL and create database  
#  
WORKDIR /database/  
COPY ./mysql/ .  
RUN service mysql start; \  
mysqladmin -u root password superInsecure; \  
rm -rf \  
/tmp/* \  
/var/tmp/*  
  
################################################################################  
# Runit service scripts  
################################################################################  
# Startup - mongo  
#  
RUN SERVICE=mongod;\  
mkdir -p /etc/service/${SERVICE}/; \  
SCRIPT=/etc/service/${SERVICE}/run; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Start mongod"; \  
echo "#"; \  
echo "mkdir -p /volumes/mongo/"; \  
echo "chown -R mongodb:mongodb /volumes/mongo/"; \  
echo "exec /sbin/setuser mongodb numactl --interleave=all mongod
--storageEngine wiredTiger --dbpath /volumes/mongo/"; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}  
  
# Startup - autossh tunnel  
#  
RUN SERVICE=autossh_prod;\  
mkdir -p /etc/service/${SERVICE}/; \  
SCRIPT=/etc/service/${SERVICE}/run; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Set variables"; \  
echo "#"; \  
echo "GATEWAY_ID=\${GATEWAY_ID:-0}"; \  
echo "TEST_OPT_IN=\${TEST_OPT_IN:-no}"; \  
echo "#"; \  
echo "IP_COMPOSER=\${IP_COMPOSER:-142.104.128.120}"; \  
echo "PORT_AUTOSSH=\${PORT_AUTOSSH:-2774}"; \  
echo "PORT_START_GATEWAY=\${PORT_START_GATEWAY:-40000}"; \  
echo "PORT_REMOTE=\\`expr \${PORT_START_GATEWAY} + \${GATEWAY_ID}\\`"; \  
echo "#"; \  
echo "VOLUME_SSH=/volumes/ssh"; \  
echo ""; \  
echo ""; \  
echo "# Check for SSH keys"; \  
echo "#"; \  
echo "mkdir -p \${VOLUME_SSH}/"; \  
echo "chown -R autossh:autossh \${VOLUME_SSH}"; \  
echo "if [ ! -s \${VOLUME_SSH}/id_rsa.pub ]"; \  
echo "then"; \  
echo " ssh-keygen -b 4096 -t rsa -N \"\" -C ep\${GATEWAY_ID}-\$(date
+%Y-%m-%d-%T) -f \${VOLUME_SSH}/id_rsa"; \  
echo "fi"; \  
echo ""; \  
echo ""; \  
echo "# Start tunnels"; \  
echo "#"; \  
echo "export AUTOSSH_MAXSTART=1"; \  
echo "#"; \  
echo "/sbin/setuser autossh /usr/bin/autossh \${IP_COMPOSER} -p
\${PORT_AUTOSSH} -i \${VOLUME_SSH}/id_rsa \\\"; \  
echo " -N -R \${PORT_REMOTE}:localhost:3001 -o ServerAliveInterval=15 -o
Protocol=2\\\"; \  
echo " -o ServerAliveCountMax=3 -o ExitOnForwardFailure=yes -o
StrictHostKeyChecking=no"; \  
echo ""; \  
echo ""; \  
echo "# If connection has failed, provide direction"; \  
echo "#"; \  
echo "cat \${VOLUME_SSH}/id_rsa.pub"; \  
echo "echo"; \  
echo "echo 'AutoSSH not connected. Please provide \${VOLUME_SSH}/id_rsa.pub
(above),'"; \  
echo "echo 'a list of participating CPSIDs and all paperwork to the PDC at
admin@pdcbc.ca'"; \  
echo "sleep 60"; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}  
  
# Startup - autossh testing tunnel (optional)  
#  
RUN SERVICE=autossh_test;\  
mkdir -p /etc/service/${SERVICE}/; \  
SCRIPT=/etc/service/${SERVICE}/run; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Set variables"; \  
echo "#"; \  
echo "GATEWAY_ID=\${GATEWAY_ID:-0}"; \  
echo "TEST_OPT_IN=\${TEST_OPT_IN:-no}"; \  
echo "#"; \  
echo "IP_TESTCPSR=\${IP_TESTCPSR:-142.104.128.121}"; \  
echo "PORT_AUTOSSH=\${PORT_AUTOSSH:-2774}"; \  
echo "PORT_START_GATEWAY=\${PORT_START_GATEWAY:-40000}"; \  
echo "PORT_REMOTE=\\`expr \${PORT_START_GATEWAY} + \${GATEWAY_ID}\\`"; \  
echo "#"; \  
echo "VOLUME_SSH=/volumes/ssh"; \  
echo ""; \  
echo ""; \  
echo "# Start tunnels"; \  
echo "#"; \  
echo "sleep 15"; \  
echo "export AUTOSSH_MAXSTART=1"; \  
echo "#"; \  
echo "if [ \${TEST_OPT_IN} == yes ]"; \  
echo "then"; \  
echo " export AUTOSSH_MAXSTART=2"; \  
echo " /sbin/setuser autossh /usr/bin/autossh \${IP_TESTCPSR} -p
\${PORT_AUTOSSH} -i \${VOLUME_SSH}/id_rsa \\\"; \  
echo " -N -R \${PORT_REMOTE}:localhost:3001 -o ServerAliveInterval=15 -o
Protocol=2 \\\"; \  
echo " -o ServerAliveCountMax=3 -o ExitOnForwardFailure=yes -o
StrictHostKeyChecking=no"; \  
echo "else"; \  
echo " rm -rf /etc/service/"${SERVICE}; \  
echo "fi"; \  
echo "sleep 60"; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}  
  
# Startup - gateway delayed job  
#  
RUN SERVICE=delayed_job;\  
mkdir -p /etc/service/${SERVICE}/; \  
SCRIPT=/etc/service/${SERVICE}/run; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Start delayed job"; \  
echo "#"; \  
echo "cd /gateway/"; \  
echo "/sbin/setuser app bundle exec /gateway/script/delayed_job stop >
/dev/null"; \  
echo "rm /gateway/tmp/pids/server.pid > /dev/null"; \  
echo "exec /sbin/setuser app bundle exec /gateway/script/delayed_job run"; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}  
  
# Startup - gateway rails server  
#  
RUN SERVICE=rails;\  
mkdir -p /etc/service/${SERVICE}/; \  
SCRIPT=/etc/service/${SERVICE}/run; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Set variables"; \  
echo "#"; \  
echo "DOCTOR_IDS=\${DOCTOR_IDS:-cpsid}"; \  
echo ""; \  
echo ""; \  
echo "# Populate providers.txt with DOCTOR_IDS"; \  
echo "#"; \  
echo "/gateway/providers.sh add \${DOCTOR_IDS}"; \  
echo ""; \  
echo ""; \  
echo "# Start Rails server"; \  
echo "#"; \  
echo "cd /gateway/"; \  
echo "exec /sbin/setuser app bundle exec rails server -p 3001"; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}  
  
################################################################################  
# Scripts and Crontab  
################################################################################  
# SSH test  
#  
RUN SCRIPT=/ssh_test.sh; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Attempt to connect autossh tunnel and notify user"; \  
echo "#"; \  
echo "sleep 5"; \  
echo "echo"; \  
echo "echo"; \  
echo "if [ \"\$( setuser autossh ssh -i /volumes/ssh/id_rsa -p 2774
142.104.128.120 /app/test/ssh_landing.sh )\" ]"; \  
echo "then"; \  
echo " echo 'Connection successful!'"; \  
echo " echo"; \  
echo " echo ':D'"; \  
echo "else"; \  
echo " cat /volumes/ssh/id_rsa.pub"; \  
echo " echo 'ERROR: unable to connect to 142.104.128.120'"; \  
echo " echo"; \  
echo " echo 'Please verify the ssh public key (above) has been provided to
admin@pdcbc.ca.'"; \  
echo "fi"; \  
echo "echo"; \  
echo "echo"; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}  
  
# Cron script - db maintenance  
#  
RUN SCRIPT=/db_maintenance.sh; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Wait for mongo to start"; \  
echo "#"; \  
echo "while [ \$( pgrep -c mongod ) -eq 0 ]"; \  
echo "do"; \  
echo " sleep 60"; \  
echo "done"; \  
echo "sleep 5"; \  
echo ""; \  
echo ""; \  
echo "# Set index"; \  
echo "#"; \  
echo "/usr/bin/mongo query_gateway_development --eval 'printjson(
db.records.ensureIndex({ hash_id : 1 }, { unique : true }))'"; \  
echo ""; \  
echo ""; \  
echo "# Database junk cleanup"; \  
echo "#"; \  
echo "/usr/bin/mongo query_gateway_development --eval 'db.providers.drop()' ||
true"; \  
echo "/usr/bin/mongo query_gateway_development --eval 'db.queries.drop()'"; \  
echo "/usr/bin/mongo query_gateway_development --eval 'db.results.drop()'"; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}  
  
# Cron script - OSCAR SQL/E2E import/export  
#  
RUN SCRIPT=/run_export.sh; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Set variables"; \  
echo "#"; \  
echo "E2E_DIFF=\${E2E_DIFF:-off}"; \  
echo "E2E_DIFF_DAYS=\${E2E_DIFF_DAYS:-14}"; \  
echo ""; \  
echo ""; \  
echo "# Configure oscar12.properties"; \  
echo "#"; \  
echo 'sed -i \'; \  
echo ' -e "s/^#*E2E_DIFF *=.*/E2E_DIFF = ${E2E_DIFF}/" \'; \  
echo ' -e "s/^#*E2E_DIFF_DAYS *=.*/E2E_DIFF_DAYS = ${E2E_DIFF_DAYS}/" \'; \  
echo "/usr/share/tomcat6/oscar12.properties"; \  
echo ""; \  
echo ""; \  
echo "# Start MySQL and import dumps"; \  
echo "#"; \  
echo "service mysql start"; \  
echo "echo Preparing oscar_12_1"; \  
echo "echo drop"; \  
echo "mysql --user=root --password=superInsecure -e 'drop database
oscar_12_1;' || true"; \  
echo "echo create"; \  
echo "mysql --user=root --password=superInsecure -e 'create database
oscar_12_1;'"; \  
echo "mysql --user=root --password=superInsecure -e 'set autocommit=0;'"; \  
echo "mysql --user=root --password=superInsecure -e 'set unique_checks=0;'"; \  
echo "mysql --user=root --password=superInsecure -e 'set
foreign_key_checks=0;'"; \  
echo "echo import base"; \  
echo "mysql --user=root --password=superInsecure oscar_12_1 <
/database/oscar_12_1.sql"; \  
echo "mysql --user=root --password=superInsecure -e 'commit;'"; \  
echo "echo import clinic"; \  
echo 'find /volumes/import/ -name "*.sql" | \'; \  
echo " while read IN"; \  
echo " do"; \  
echo ' mysql --user=root --password=superInsecure oscar_12_1 < "${IN}"'; \  
echo " done"; \  
echo "mysql --user=root --password=superInsecure -e 'commit;'"; \  
echo ""; \  
echo ""; \  
echo "# Start Tomcat6"; \  
echo "#"; \  
echo "echo tomcat"; \  
echo "mkdir -p /tmp/tomcat6-tmp/"; \  
echo "/sbin/setuser tomcat6 /usr/lib/jvm/java-6-oracle/bin/java \\\"; \  
echo "
-Djava.util.logging.config.file=/var/lib/tomcat6/conf/logging.properties \\\";
\  
echo " -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager \\\";
\  
echo " -Djava.awt.headless=true -Xmx1024m -Xms1024m -XX:MaxPermSize=512m
-server \\\"; \  
echo " -Djava.endorsed.dirs=/usr/share/tomcat6/endorsed -classpath
/usr/share/tomcat6/bin/bootstrap.jar \\\"; \  
echo " -Dcatalina.base=/var/lib/tomcat6 -Dcatalina.home=/usr/share/tomcat6
\\\"; \  
echo " -Djava.io.tmpdir=/tmp/tomcat6-tmp org.apache.catalina.startup.Bootstrap
start"; \  
echo "#"; \  
echo "mysql --user=root --password=superInsecure -e 'drop database
oscar_12_1;'"; \  
echo "service mysql stop"; \  
) \  
>> ${SCRIPT}; \  
chmod +x ${SCRIPT}  
  
# Crontab  
#  
RUN ( \  
echo "# Run maintenance script (boot, Sundays at 12 PST = 20 UTC)"; \  
echo "@reboot /db_maintenance.sh"; \  
echo "0 20 * * 0 /db_maintenance.sh"; \  
echo ""; \  
echo "# Run SQL/E2E import/export (boot, daily 3:30 PST = 4:30 PDT = 11:30
UTC)"; \  
echo "@reboot /run_export.sh > /import.log"; \  
echo "30 11 * * * /run_export.sh > /import.log"; \  
) \  
| crontab -  
  
################################################################################  
# Volumes, ports and start command  
################################################################################  
# Volumes  
#  
RUN mkdir -p \  
/volumes/import/ \  
/volumes/mongo/ \  
/volumes/ssh/; \  
chown -R mongodb:mongodb /volumes/mongo/; \  
chown -R autossh:autossh /volumes/ssh/  
VOLUME /volumes/  
  
# Initialize  
#  
WORKDIR /  
CMD ["/sbin/my_init"]  
  
################################################################################  
# Temporary fix until ssh bug is patched
(http://undeadly.org/cgi?action=article&sid=20160114142733)  
################################################################################  
RUN ( \  
echo ""; \  
echo "# Temporary ssh bug fix"; \  
echo "# "; \  
echo "Host *"; \  
echo "UseRoaming no"; \  
) | tee -a /etc/ssh/ssh_config  

