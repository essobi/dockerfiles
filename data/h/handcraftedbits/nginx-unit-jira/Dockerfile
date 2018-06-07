FROM handcraftedbits/nginx-unit:1.1.3  
MAINTAINER HandcraftedBits <opensource@handcraftedbits.com>  
  
ARG JIRA_VERSION=7.3.3  
ENV JIRA_HOME /opt/data/jira  
  
RUN apk update && \  
apk add ca-certificates openjdk8-jre wget && \  
  
cd /opt && \  
wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-
software-${JIRA_VERSION}.tar.gz && \  
tar -xzvf atlassian-jira-software-${JIRA_VERSION}.tar.gz && \  
rm atlassian-jira-software-${JIRA_VERSION}.tar.gz && \  
mv atlassian-jira-software-${JIRA_VERSION}-standalone jira && \  
  
apk del wget  
  
COPY data /  
  
EXPOSE 8080  
CMD [ "/bin/bash", "/opt/container/script/run-jira.sh" ]  

