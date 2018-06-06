#Dockerfile for Atlassian CLI  
FROM openjdk:8-jdk-alpine  
ADD
https://bobswift.atlassian.net/wiki/download/attachments/16285777/atlassian-
cli-7.9.0-SNAPSHOT-
distribution.zip?version=3&modificationDate=1522893347365&cacheVersion=1&api=v2
/opt/atlassian_cli.zip  
RUN unzip /opt/atlassian_cli.zip -d /opt/  
RUN rm /opt/atlassian_cli.zip  
RUN mv /opt/atlassian-cli*/ /opt/atlassian-cli/  
RUN mkdir /export/  
RUN mkdir /opt/logs  
RUN mkdir /opt/test  
ENV PATH="/opt/atlassian-cli:${PATH}"  
WORKDIR /opt/atlassian-cli  

