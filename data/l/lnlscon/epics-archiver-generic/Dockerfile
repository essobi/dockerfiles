#  
# Docker image for a general EPICS Archiver Appliance. It consists of  
# the base image for the mgmt, etl, engine and retrieval Docker containers.  
#  
# Gustavo Ciotto Pinton  
# LNLS - Brazilian Synchrotron Light Source  
# Controls Group  
#  
# TODO: Remove source files required to build the image. It are kept for now
only for developmente purposes.  
#  
FROM tomcat:9  
MAINTAINER Gustavo Ciotto  
  
# User root is required to install all needed packages  
USER root  
  
# Updates default image and install required packages  
RUN apt-get -y update && \  
apt-get install -y ant gcc git g++ libreadline-dev make openjdk-8-jdk perl tar
xmlstarlet wget && \  
rm -rf /var/lib/apt/lists/*  
  
ENV APPLIANCE_NAME epics-archiver-appliances  
ENV APPLIANCE_FOLDER /opt/${APPLIANCE_NAME}  
  
RUN mkdir -p ${APPLIANCE_FOLDER}/build/scripts  
  
# General EPICS Archiver Appliance Setup  
ENV ARCHAPPL_SITEID lnls-control-archiver  
  
# EPICS environment variables  
ENV EPICS_BASE_VERSION 3.15.5  
ENV EPICS_BASE_TAR_NAME base-${EPICS_BASE_VERSION}  
ENV EPICS_BASE_NAME base-${EPICS_BASE_VERSION}  
ENV EPICS_BASE_URL
https://epics.anl.gov/download/base/${EPICS_BASE_TAR_NAME}.tar.gz  
ENV EPICS_INSTALL_DIR /opt  
  
ENV EPICS_HOST_ARCH linux-x86_64  
ENV EPICS_INSTALL_DIR /opt/base-3.14.12.6/bin/${EPICS_HOST_ARCH}  
ENV EPICS_BASE ${EPICS_INSTALL_DIR}/${EPICS_BASE_NAME}  
ENV PATH ${EPICS_INSTALL_DIR}/${EPICS_BASE_NAME}/bin/${EPICS_HOST_ARCH}:$PATH  
  
COPY env-vars.sh \  
setup-epics.sh \  
${APPLIANCE_FOLDER}/build/scripts/  
  
# Install EPICS base  
RUN ${APPLIANCE_FOLDER}/build/scripts/setup-epics.sh  
  
# Github repository variables  
ENV GITHUB_APPLIANCES_BRANCH ldap-login  
ENV GITHUB_REPOSITORY_FOLDER /opt/epicsarchiverap-ldap  
ENV GITHUB_REPOSITORY_URL https://github.com/lnls-sirius/epicsarchiverap-
ldap.git  
  
# Clone archiver github's repository  
RUN git clone \--branch=${GITHUB_APPLIANCES_BRANCH} ${GITHUB_REPOSITORY_URL}
${GITHUB_REPOSITORY_FOLDER}  
  
RUN mkdir -p ${APPLIANCE_FOLDER}/build/bin  
  
### Set up mysql connector  
ENV MYSQL_CONNECTOR mysql-connector-java-5.1.41  
RUN wget -P ${APPLIANCE_FOLDER}/build/bin
https://dev.mysql.com/get/Downloads/Connector-J/${MYSQL_CONNECTOR}.tar.gz  
  
RUN tar -C ${APPLIANCE_FOLDER}/build/bin -xvf
${APPLIANCE_FOLDER}/build/bin/${MYSQL_CONNECTOR}.tar.gz  
  
RUN cp
${APPLIANCE_FOLDER}/build/bin/${MYSQL_CONNECTOR}/${MYSQL_CONNECTOR}-bin.jar
${CATALINA_HOME}/lib  
  
RUN rm -R ${APPLIANCE_FOLDER}/build/bin/${MYSQL_CONNECTOR}/  
  
RUN mkdir -p ${APPLIANCE_FOLDER}/configuration  
  
RUN mkdir -p ${APPLIANCE_FOLDER}/storage  
  
# ARCHAPPL_APPLIANCES is always the same for every image, but
ARCHAPPL_MYIDENTITY is not. So it needs to be  
# defined when the container is started  
ENV ARCHAPPL_APPLIANCES ${APPLIANCE_FOLDER}/configuration/lnls_appliances.xml  
ENV ARCHAPPL_POLICIES ${APPLIANCE_FOLDER}/configuration/lnls_policies.py  
ENV ARCHAPPL_SHORT_TERM_FOLDER ${APPLIANCE_FOLDER}/storage/sts  
ENV ARCHAPPL_MEDIUM_TERM_FOLDER ${APPLIANCE_FOLDER}/storage/mts  
ENV ARCHAPPL_LONG_TERM_FOLDER ${APPLIANCE_FOLDER}/storage/lts  
  
RUN mkdir -p ${ARCHAPPL_SHORT_TERM_FOLDER}  
RUN mkdir -p ${ARCHAPPL_MEDIUM_TERM_FOLDER}  
RUN mkdir -p ${ARCHAPPL_LONG_TERM_FOLDER}  
  
RUN mkdir -p ${APPLIANCE_FOLDER}/build/configuration/wait-for-it  
RUN git clone https://github.com/vishnubob/wait-for-it.git
${APPLIANCE_FOLDER}/build/configuration/wait-for-it  
  

