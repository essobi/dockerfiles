# Start with Tomcat 7  
FROM tomcat:7-jre7  
MAINTAINER Progress Software <corticon-docker@progress.com>  
  
# Add custom tomcat options for Corticon  
ADD setenv.sh /usr/local/tomcat/bin  
  
# Create the Corticon work directories and the CcServerSandbox and run the
container as a swuser  
RUN mkdir -p /opt/corticon/work/cdd && \  
mkdir -p /opt/corticon/work/CcServerSandbox/ServerConsole && \  
groupadd -r swuser -g 433 && \  
useradd -u 431 -r -g swuser -d /opt/corticon/work -s /sbin/nologin -c "Docker
image user" swuser && \  
chown -R swuser:swuser /opt/corticon/work /usr/local/tomcat  
  
# Change to swuser  
USER swuser  
  
# Open port 8080  
EXPOSE 8080  
  
# Define Corticon home and work directories  
ENV CORTICON_HOME /opt/corticon  
ENV CORTICON_WORK_DIR /opt/corticon/work  
  
# Add Corticon War to the image  
ADD axis.war /opt/corticon/

