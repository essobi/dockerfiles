FROM centos:centos7  
MAINTAINER Rory Donohue <rory@kindeo.com>  
  
# Environment vars  
ENV APP_DEST_DIR "/home/kindeo-api"  
ENV APP_PORT 8000  
ENV APP_USER "web-user"  
# Update the system  
RUN yum -y update && yum clean all  
  
# Install some basic tools  
RUN yum install -y net-tools vim-enhanced  
  
# Enable Extra Packages for Enterprise Linux (EPEL) for CentOS  
RUN yum install -y epel-release  
  
# Install Node.js and npm  
RUN yum install -y nodejs npm  
  
# Bundle app source  
RUN mkdir ${APP_DEST_DIR}  
COPY . ${APP_DEST_DIR}  
  
# Set the workdir for commands that follow  
WORKDIR ${APP_DEST_DIR}  
RUN npm install --production  
  
# Add a non-privileged user for running the web app  
RUN useradd ${APP_USER}  
RUN chown -R ${APP_USER} ${APP_DEST_DIR}  
  
EXPOSE ${APP_PORT}  
  
# Run the node server as a non-privileged user  
USER ${APP_USER}  
  
# Default for the executing container  
CMD ["node", "server.js"]  

