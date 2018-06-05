#  
# Docker image for Apache ActiveMQ, used by the communication between alarm  
# server and clients.  
#  
# Gustavo Ciotto Pinton  
# Controls Group - Brazilian Synchrotron Light Source Laboratory - LNLS  
#  
FROM debian:stretch  
  
MAINTAINER Gustavo Ciotto  
  
ENV SCRIPT_FOLDER /opt/activemq  
  
RUN mkdir -p ${SCRIPT_FOLDER}/scripts/  
  
# Update image and install required packages  
RUN apt-get -y update && \  
apt-get install -y activemq && \  
rm -rf /var/lib/apt/lists/*  
  
COPY activemq-start \  
${SCRIPT_FOLDER}/scripts/  
  
WORKDIR ${SCRIPT_FOLDER}/scripts/  
  
RUN mkdir /etc/activemq/instances-enabled/main  
  
# Copy activemq configuration file into the image  
COPY activemq.xml /etc/activemq/instances-enabled/main  
  
CMD ["sh", "-c", "${SCRIPT_FOLDER}/scripts/activemq-start"]  

