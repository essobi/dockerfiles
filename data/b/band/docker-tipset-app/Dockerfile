FROM centos:7  
  
MAINTAINER Bosse Andersson  
  
RUN useradd \--shell=/bin/bash \--home=/home/tipset tipset  
RUN yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-headless  
  
USER tipset  
  
ENV SPRING_PROFILES_ACTIVE="prod,postgres"  
ENV
SPRING_CONFIG_LOCATION="classpath:/application.yml,/home/tipset/application.yml"  
  
EXPOSE 8443  
  
# This container needs a volume at /home/tipset containing  
# the tipset-war file and deployment specific configuration.  
# Java options can be controlled using the standard _JAVA_OPTIONS or  
# JAVA_TOOL_OPTIONS variables.  
ENTRYPOINT [ "/usr/bin/java", "-jar", "/home/tipset/tipset.war" ]  

