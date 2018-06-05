#Dockerfile for Atlassian CLI  
FROM openjdk:8-jre-alpine  
#Add necessary packages to default image  
RUN apk add --no-cache bash coreutils curl  
ADD
https://marketplace.atlassian.com/download/plugins/org.swift.atlassian.cli/version/780
/opt/atlassian_cli.zip  
RUN unzip /opt/atlassian_cli.zip -d /opt/  
RUN rm /opt/atlassian_cli.zip  
RUN mv /opt/atlassian-cli*/ /opt/atlassian-cli/  
ENV PATH="/opt/atlassian-cli:${PATH}"  
WORKDIR /opt/atlassian-cli  

