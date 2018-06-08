FROM openjdk:8-jdk  
MAINTAINER Software Craftsmen GmbH und CoKG <martin.ahrer@software-
craftsmen.at>  
  
# BEGIN install atlassian plugin sdk  
  
RUN apt-get update && \  
curl https://packages.atlassian.com/list/atlassian-sdk-deb/deb-
archive/atlassian-plugin-sdk_6.3.7_all.deb -O && \  
dpkg -i atlassian-plugin-sdk_6.3.7_all.deb  

