#!/usr/bin/docker  
# based on Ubuntu  
FROM stormsw/ubuntu-java:Oracle-Java8  
MAINTAINER Alexander Varchenko <alexander.varchenko@gmail.com>  
# Aumentum-WildFly:8.2  
# Create a user and group used to launch processes  
# The user ID 1000 is the default for the first user on Debian/Ubuntu,  
# so there is a high chance that this ID will be equal to the current user  
# making it easier to use volumes (no permission issues)  
RUN groupadd -r jboss -g 1000 && useradd -u 1000 -r -g jboss -m -d /opt/jboss
-s /sbin/nologin -c "JBoss user" jboss  
# Set the working directory to jboss' user home directory  
WORKDIR /opt/jboss  
# Specify the user which should be used to execute all commands below  
USER jboss  
#export Java home for JBoss user  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
#=======================================  
# Wildfly part  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 8.2.0.Final  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME && \  
curl -L
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| \  
tar zx && \  
mv $HOME/wildfly-$WILDFLY_VERSION $HOME/wildfly  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/jboss/wildfly  
# add default admin:admin user (We are set SIMPLE not RBAC mode in the
batch.cli)  
RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent  
  
#JDBC integration part  
#Integrate POSTGRESQL jdbc driver  
RUN curl -L -o /tmp/psql-jdbc.jar
http://jdbc.postgresql.org/download/postgresql-9.3-1102.jdbc41.jar  
#Integrate SQL Server/Sybase driver  
RUN curl -L -o /tmp/jdts-1.3.1-dist.zip
http://sourceforge.net/projects/jtds/files/jtds/1.3.1/jtds-1.3.1-dist.zip/download
&& \  
unzip -p /tmp/jdts-1.3.1-dist.zip jtds-1.3.1.jar>/tmp/jtds-1.3.1.jar  
#integrate Oracle driver  
COPY jdbc/oracle/ /tmp/  
#integrate MySQL driver  
ADD jdbc/mysql/mysql-connector-java-5.1.35-bin.jar /tmp/  
ADD jdbc/mssql/sqljdbc_4.0/enu/sqljdbc4.jar /tmp/  
#register modules and datasources  
# please chek alternatives on https://goldmann.pl/blog/2014/07/23/customizing-
the-configuration-of-the-wildfly-docker-image/  
# the tools described are included in this image  
ADD config.sh /tmp/  
ADD batch.cli /tmp/  
RUN /tmp/config.sh  
USER root  
# Fix for Error: Could not rename
/opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current  
RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history
&&\  
rm /tmp/*.jar &&\  
rm /tmp/*.zip  
# this is commented cause wildfly-debug package may reuse this  
#rm /tmp/config.sh &&\  
#rm /tmp/batch.cli  
ENV DEBIAN_FRONTEND newt  
USER jboss  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0",
"-bmanagement","0.0.0.0"]  

