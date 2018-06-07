# Jersey-skeleton's Dockerfile =================================  
# Release under MIT Licence  
# For more information, visit github.com/maugern/jersey-skeleton  
# DEFINE IMAGE =================================================  
FROM debian:jessie  
MAINTAINER Nicolas Mauger <https://github.com/maugern/>  
  
# BEFORE INSTALL ===============================================  
# Sets language to UTF8 : this works in pretty much all cases  
ENV LANG en_US.UTF-8  
RUN apt-get update  
  
# INSTALL JAVA 7 ===============================================  
RUN apt-get install --fix-missing -y -f openjdk-7-jdk  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64  
ENV PATH $PATH:$JAVA_HOME/bin  
ENV CLASSPATH $JAVA_HOME/lib/tools.jar  
  
# INSTALL & CONFIGURE MAVEN ====================================  
RUN apt-get install -y --force-yes maven  
ADD pom.xml /srv/jersey-skeleton/  
WORKDIR /srv/jersey-skeleton/  
RUN mvn install  
  
# SQLITE & database ============================================  
RUN apt-get install -y --force-yes sqlite3  
  
# Add database init script & run it  
ADD tools/database_creation.sql /srv/jersey-skeleton/tools/  
ADD tools/database_purge.sql /srv/jersey-skeleton/tools/  
RUN sqlite3 /tmp/data.db < /srv/jersey-skeleton/tools/database_creation.sql  
  
# Add database epuration scipt and run it via cron  
ADD tools/crontab /etc/cron.d/database-cron  
RUN chmod 0644 /etc/cron.d/database-cron  
RUN touch /var/log/cron.log  
CMD cron && tail -f /var/log/cron.log  
  
# WEB SERVICE CONFIGURATION ====================================  
# Precise the source folder  
ADD src /srv/jersey-skeleton/src/  
# Listen on the specified network port  
EXPOSE 8080  
# START THE WED SERVER =========================================  
CMD mvn jetty:run  

