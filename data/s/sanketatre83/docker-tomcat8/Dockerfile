FROM ubuntu:14.04  
  
# Set locales  
RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LC_CTYPE en_GB.UTF-8  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y git build-essential curl wget software-properties-common
default-jdk ant git  
  
# Get Tomcat  
RUN apt-get update && \  
apt-get install -y tomcat7  
  
# Add admin/admin user  
ADD tomcat-users.xml /opt/tomcat/conf/  
  
  
# Launch Tomcat  
CMD service tomcat7 start  

