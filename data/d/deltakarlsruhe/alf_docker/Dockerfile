######################################################################  
# Dockerfile  
# Author: Matt Ward  
# Date: 28 December 2014  
#  
# Alfresco server docker image.  
#  
# Repository, Solr and Share all-in-one image prototype.  
# This server expects a Postgres DB to be available.  
#  
# NOT FOR PRODUCTION USE!  
#  
######################################################################  
FROM ubuntu:14.04  
MAINTAINER Matt Ward <matt.ward@alfresco.com>  
  
ENV ALF_VER 20151217-SNAPSHOT-591  
ENV ALF_INSTALLER_BIN AlfrescoCommunity.bin  
ENV ALF_INSTALL_OPTIONS_FILE install_options.txt  
ENV ALF_INSTALLER_DIR /alfresco/installer  
ENV ALFRESCO_HOME /opt/alfresco-community  
ENV ALF_PROPS_FILE $ALFRESCO_HOME/tomcat/shared/classes/alfresco-
global.properties  
ENV ALF_INSTALLER_DOWNLOADER getCommunityEdition.sh  
  
  
RUN apt-get update  
# install OpenOffice requirements so that transformation work ok  
RUN apt-get install -y libxext6 libc6 libfreetype6 libx11-6 libxau6 libxdmcp6
libxinerama1 libcups2 libdbus-glib-1-2 libfontconfig1 wget  
# Other utilities  
#RUN apt-get install -y hostname  
RUN mkdir -p $ALF_INSTALLER_DIR  
  
ADD $ALF_INSTALLER_DOWNLOADER $ALF_INSTALLER_DIR/  
# ADD $ALF_INSTALLER_BIN $ALF_INSTALLER_DIR/ Not yet existing  
ADD $ALF_INSTALL_OPTIONS_FILE $ALF_INSTALLER_DIR/  
  
WORKDIR $ALF_INSTALLER_DIR  
RUN chmod +x $ALF_INSTALLER_DOWNLOADER  
# Download fresh copy of community edition installer  
RUN ./$ALF_INSTALLER_DOWNLOADER  
  
RUN chmod +x $ALF_INSTALLER_BIN  
RUN ./$ALF_INSTALLER_BIN \--optionfile $ALF_INSTALL_OPTIONS_FILE  
  
EXPOSE 8080 7070 5701  
WORKDIR $ALFRESCO_HOME  
  
RUN mkdir /alfresco/data  
RUN sed -i 's:^[ \t]*dir.root[ \t]*=\\([
\t]*.*\\)$:dir.root='/alfresco/data':' $ALF_PROPS_FILE  
  
# Change dir.keystore to point to installed keystore - would be nicer to ADD
the keystore  
# to the data volume  
RUN sed -i 's:^[ \t]*dir.keystore[ \t]*=\\([
\t]*.*\\)$:dir.keystore='${ALFRESCO_HOME}/alf_data/keystore':' $ALF_PROPS_FILE  
  
# Ensure a log file exists ready for tail  
RUN touch $ALFRESCO_HOME/alfresco.log  
  
# Logging  
ADD dev-log4j.properties
$ALFRESCO_HOME/tomcat/shared/classes/alfresco/extension/  
  
# Deploy custom war files  
#ADD *.war $ALFRESCO_HOME/tomcat/webapps/  
# Install a license file if one exists no licences for community edition  
# ADD *.lic $ALFRESCO_HOME/tomcat/shared/classes/alfresco/extension/license/  
# Use instead of alfresco.sh -- but it will invoke it.  
# This is only when starting the container, it is fine to run alfresco.sh to
start and stop  
# Alfresco once the container has been initialised.  
ADD docker_start $ALFRESCO_HOME/  
RUN chmod +x $ALFRESCO_HOME/docker_start  
  
# Run the container's process!  
CMD /bin/bash -c $ALFRESCO_HOME/docker_start  
  

