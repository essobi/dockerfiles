#  
# Docker image for BEAST Alarm Server  
#  
# Author: Gustavo Ciotto Pinton  
# LNLS - Brazilian Synchrotron Light Source Laboratory  
#  
FROM openjdk:latest  
  
MAINTAINER Gustavo Ciotto <gustavo.pinton@lnls.br>  
  
# Github environment variables  
ENV GITHUB_ALARM_REPO
https://github.com/ControlSystemStudio/org.csstudio.alarmserver.product.git  
ENV GITHUB_ALARM_BRANCH master  
  
# Alarm operation-related variables  
ENV ALARM_FOLDER /opt/lnls-alarm-server  
ENV ALARM_VERSION beast-alarm-server-4.1.1  
# Update image and install required packages  
RUN apt-get -y update && apt-get install -y git maven openjdk-8-jdk
postgresql-client && rm -rf /var/lib/apt/lists/*  
  
# create new folder and copy all scripts  
RUN mkdir -p ${ALARM_FOLDER}/build/scripts/  
  
COPY scripts/setup-beast.sh ${ALARM_FOLDER}/build/scripts/  
  
# Clone and compile alarm source code  
RUN ${ALARM_FOLDER}/build/scripts/setup-beast.sh  
  
# Copy provided configuration file  
COPY configuration/LNLS-CON.ini ${ALARM_FOLDER}/${ALARM_VERSION}/configuration  
  
RUN mkdir ${ALARM_FOLDER}/${ALARM_VERSION}/scripts  
  
RUN mkdir -p ${ALARM_FOLDER}/${ALARM_VERSION}/log  
  
RUN mkdir -p ${ALARM_FOLDER}/${ALARM_VERSION}/scripts/wait-for-it  
  
RUN git clone https://github.com/vishnubob/wait-for-it.git
${ALARM_FOLDER}/${ALARM_VERSION}/scripts/wait-for-it  
  
COPY scripts/start-beast.sh ${ALARM_FOLDER}/${ALARM_VERSION}/scripts  
  
CMD ["sh", "-c", "${ALARM_FOLDER}/${ALARM_VERSION}/scripts/start-beast.sh"]  

