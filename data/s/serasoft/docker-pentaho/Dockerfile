#  
# Serasoft's docker image for Pentaho Business Analytics  
#  
# VERSION 1.2  
#  
FROM serasoft/docker-jdk:jdk8  
MAINTAINER Sergio Ramazzina, sergio.ramazzina@serasoft.it  
  
# Set correct environment variables.  
ENV HOME /root  
ENV PENTAHO_HOME /opt/pentaho  
ENV TOMCAT_HOME ${PENTAHO_HOME}/biserver-ce/tomcat  
ENV PLUGIN_SET marketplace,cdf,cda,cde,cgg  
ENV BASE_REL 6.0  
ENV REV 1.0-386  
# Set default metadata DB to postgresql  
ENV DB_TYPE postgresql  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# =============================== Start Image Customization
===================  
# Make sure base image is updatet then install needed linux tools  
# Install latest postgresql version as pentaho metadata repository  
RUN echo deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main >>
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
apt-get update && \  
apt-get upgrade -f -y && \  
apt-get install -f -y wget curl git zip pwgen postgresql-9.4  
  
# Workaround for bug  
# https://github.com/helmi03/docker-postgis/issues/10  
# https://github.com/docker/docker/issues/783  
RUN echo "mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-
copy/; rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private;
chmod -R 0700 /etc/ssl/private; chown -R postgres /etc/ssl/private" >>
/etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Configure postgresql to run with locally installed pentaho instance  
ADD v5/db/pg_hba.conf /etc/postgresql/9.4/main/pg_hba.conf  
RUN chown postgres:postgres /etc/postgresql/9.4/main/pg_hba.conf  
  
RUN useradd -m -d ${PENTAHO_HOME} pentaho  
  
RUN su -c "curl -L
http://sourceforge.net/projects/pentaho/files/Business%20Intelligence%20Server/${BASE_REL}/biserver-
ce-${BASE_REL}.${REV}.zip/download -o /opt/pentaho/biserver-ce.zip" pentaho &&
\  
su -c "unzip -q /opt/pentaho/biserver-ce.zip -d /opt/pentaho/" pentaho && \  
rm /opt/pentaho/biserver-ce/promptuser.sh && \  
rm /opt/pentaho/biserver-ce.zip && \  
# Disable daemon mode for Tomcat so that docker logs works properly  
sed -i -e 's/\\(exec ".*"\\) start/\1 run/' /opt/pentaho/biserver-
ce/tomcat/bin/startup.sh  
  
# Remove unnecessary/broken plugins  
RUN rm -Rf /opt/pentaho/biserver-ce/pentaho-solutions/system/pentaho-jpivot-
plugin /opt/pentaho/biserver-ce/pentaho-solutions/system/marketplace  
  
# Install CTools installer and update major plugins  
RUN wget --no-check-certificate
'https://raw.githubusercontent.com/sramazzina/ctools-installer/master/ctools-
installer.sh' -P / -o /dev/null && \  
chmod +x ctools-installer.sh && \  
./ctools-installer.sh -s ${PENTAHO_HOME}/biserver-ce/pentaho-solutions -y -c
${PLUGIN_SET}  
  
# Add all files needed t properly initialize the container  
COPY utils ${PENTAHO_HOME}/biserver-ce/utils  
ADD v5/db/${DB_TYPE}/create_jcr_${DB_TYPE}.sql /opt/pentaho/biserver-
ce/data/${DB_TYPE}/create_jcr_${DB_TYPE}.sql  
ADD v5/db/${DB_TYPE}/create_quartz_${DB_TYPE}.sql /opt/pentaho/biserver-
ce/data/${DB_TYPE}/create_quartz_${DB_TYPE}.sql  
ADD v5/db/${DB_TYPE}/create_repository_${DB_TYPE}.sql /opt/pentaho/biserver-
ce/data/${DB_TYPE}/create_repository_${DB_TYPE}.sql  
ADD ./v5/db/dummy_quartz_table.sql /opt/pentaho/biserver-
ce/data/postgresql/dummy_quartz_table.sql  
  
ADD v5/pentaho/system/${DB_TYPE}/applicationContext-spring-security-
hibernate.properties /opt/pentaho/biserver-ce/pentaho-
solutions/system/applicationContext-spring-security-hibernate.properties  
ADD v5/pentaho/system/${DB_TYPE}/hibernate-settings.xml /opt/pentaho/biserver-
ce/pentaho-solutions/system/hibernate/hibernate-settings.xml  
ADD v5/pentaho/system/${DB_TYPE}/quartz.properties /opt/pentaho/biserver-
ce/pentaho-solutions/system/quartz/quartz.properties  
ADD v5/pentaho/system/${DB_TYPE}/repository.xml /opt/pentaho/biserver-
ce/pentaho-solutions/system/jackrabbit/repository.xml  
ADD v5/pentaho/system/${DB_TYPE}/postgresql.hibernate.cfg.xml
/opt/pentaho/biserver-ce/pentaho-
solutions/system/hibernate/postgresql.hibernate.cfg.xml  
  
ADD v5/tomcat/${DB_TYPE}/context.xml /opt/pentaho/biserver-
ce/tomcat/webapps/pentaho/META-INF/context.xml  
ADD v5/tomcat/web.xml /opt/pentaho/biserver-ce/tomcat/webapps/pentaho/WEB-
INF/web.xml  
  
# Set password to generated value  
RUN chown -Rf pentaho:pentaho ${PENTAHO_HOME}/biserver-ce  
ADD 02_start_postgresql.sh /etc/my_init.d/02_start_postgresql.sh  
ADD 01_init_container.sh /etc/my_init.d/01_init_container.sh  
ADD 03_init_pentaho_tables.sh /etc/my_init.d/03_init_pentaho_tables.sh  
  
ADD run /etc/service/pentaho/run  
  
RUN chmod +x /etc/my_init.d/*.sh && \  
chmod +x /etc/service/pentaho/run  
  
# Expose Pentaho and PostgreSQL ports  
EXPOSE 8080 5432  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

