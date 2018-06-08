############################################################  
# Dockerfile to build Rundeck Base Container  
# Based on: centos:6.7  
# DATE: 01/22/2016  
############################################################  
  
# Set the base image in namespace/repo format.  
# To use repos that are not on the docker hub use the
example.com/namespace/repo format.  
FROM centos:6.7  
  
# File Author / Maintainer  
MAINTAINER Rich Nason rnason@sciquest.com  
  
###################################################################  
#************************* APP VERSIONS *************************  
###################################################################  
  
  
###################################################################  
#*************** OVERRIDE ENABLED ENV VARIABLES *****************  
###################################################################  
  
ENV APP_NAME localhost  
ENV APP_PORT 4440  
  
ENV MODE filesystem  
ENV MYSQL_SERVER localhost  
ENV MYSQL_CLIENT localhost  
ENV MYSQL_DB rundeck  
ENV APP_USER admin  
ENV APP_PASS PASSw0rd  
ENV TERMTAG RUNDECK  
  
###################################################################  
#****************** ADD REQUIRED APP FILES **********************  
###################################################################  
  
# ADD Rundeck Repo and key  
  
RUN rpm --import http://rundeck.org/keys/BUILD-GPG-KEY-Rundeck.org.key && \  
rpm -Uvh http://repo.rundeck.org/latest.rpm  
  
###################################################################  
#******************* UPDATES & PRE-REQS *************************  
###################################################################  
  
# Clean, Update, and Install... then clear non English local data.  
RUN yum clean all && \  
yum -y update && \  
  
# Install required packages  
yum -y install java-1.7.0-openjdk.x86_64 java-1.7.0-openjdk-devel.x86_64
mysql-client mysql-common mysql-server rundeck && \  
export JAVA_HOME=/usr/lib/jvm/jre-1.7.0-openjdk.x86_64 && \  
  
# Remove yum cache this bad boy can be 150MBish  
yum clean all && \  
rm -fr /var/cache/*  
  
###################################################################  
#******************* APPLICATION INSTALL ************************  
###################################################################  
  
  
###################################################################  
#****************** POST DEPLOY CLEAN UP ************************  
###################################################################  
  
# Perform some clean up items and set permissions  
RUN chmod +x /etc/init.d/rundeckd  
  
###################################################################  
#***************** CONFIGURE START ITEMS ************************  
###################################################################  
  
# Add Database Scripts, and Runconfig  
ADD runconfig.sh /tmp/.runconfig.sh  
ADD mysql_setup.sql /tmp/.mysql_setup.sql  
  
# Set boot items  
RUN chmod +x /tmp/.runconfig.sh && \  
echo "/tmp/./.runconfig.sh" >> ~/.bashrc && \  
echo "[ -f /tmp/.runconfig.sh ] && rm -fr /tmp/.runconfig.sh" >> /root/.bashrc  
  
RUN echo "export JAVA_HOME=/usr/lib/jvm/jre-1.7.0-openjdk.x86_64" >>
/root/.bashrc && \  
echo "export JAVA_HOME=/usr/lib/jvm/jre-1.7.0-openjdk.x86_64" >>
/etc/skel/.bashrc && \  
echo "service rundeckd start" >> /root/.bashrc  
  
CMD /bin/bash  
  
###################################################################  
#**************** EXPOSE APPLICATION PORTS **********************  
###################################################################  
  
# Expose ports to other containers only  
EXPOSE 4440  
  
###################################################################  
#******************* OPTIONAL / LEGACY **************************  
###################################################################

