FROM camunda/camunda-docker-ci-base:latest  
MAINTAINER Christian Lipphardt <christian.lipphardt@camunda.com>  
  
# Add build files  
ADD . /build  
  
# Install latest Oracle JDK 8  
RUN /build/bin/install-oracle-jdk.sh 8  

