# Apache Drill v1.4.0 - embedded mode  
#  
# VERSION 0.1 - not for production, use at own risk  
# General instructions: https://drill.apache.org/docs/install-drill-
introduction/  
#  
  
  
#  
# Using CentOS as the base image  
#  
FROM centos  
  
MAINTAINER mkieboom @mapr.com  
  
#  
# Prerequisite: Install Java, tar and create Drill folders  
# http://doc.mapr.com/display/MapR/Preparing+Each+Node#PreparingEachNode-java  
#  
RUN yum install -y tar java-1.7.0-openjdk-devel && \  
mkdir -p /drill-scripts && \  
mkdir -p /opt/drill  
#  
# Download and Install Apache Drill  
# https://drill.apache.org/docs/installing-drill-on-linux-and-mac-os-x/  
#  
RUN curl -o apache-drill-1.4.0.tar.gz
http://apache.cs.uu.nl/drill/drill-1.4.0/apache-drill-1.4.0.tar.gz && \  
tar zxpf apache-drill-1.4.0.tar.gz -C /opt/drill  
  
#  
# Start Apache Drill in embedded mode  
# https://drill.apache.org/docs/starting-drill-on-linux-and-mac-os-x/  
#  
ADD bootstrap.sh /drill-scripts/bootstrap.sh  
RUN chown root:root /drill-scripts/bootstrap.sh && \  
chmod 700 /drill-scripts/bootstrap.sh  
ENV BOOTSTRAP /drill-scripts/bootstrap.sh  
  
#  
# Expose the Apache Drill Web UI  
# https://drill.apache.org/docs/storage-plugin-registration/  
#  
EXPOSE 8047  

