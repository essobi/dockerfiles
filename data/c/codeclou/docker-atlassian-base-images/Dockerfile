FROM codeclou/docker-oracle-jdk:8u152  
  
ENV JIRA_VERSION 7.10.0  
  
RUN addgroup -g 10777 worker && \  
adduser -h /work -H -D -G worker -u 10777 worker && \  
mkdir -p /work && \  
mkdir -p /work-private && \  
mkdir /jira && mkdir /jira-home && mkdir /jira-shared-home && \  
chown -R worker:worker /work/ && \  
chown -R worker:worker /work-private/ && \  
apk add --no-cache \  
bash \  
curl \  
tar \  
python \  
py-pip && \  
pip install shinto-cli && \  
curl -jkSL -o /opt/jira.tar.gz \  
https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-
software-${JIRA_VERSION}.tar.gz && \  
tar zxf /opt/jira.tar.gz -C /jira && \  
cd /jira && \  
ln -s atlassian-jira-software-${JIRA_VERSION}-standalone atlassian-jira-
software-latest-standalone && \  
rm /opt/jira.tar.gz && \  
chown -R worker:worker /jira && \  
chown -R worker:worker /jira-home/ && \  
chown -R worker:worker /jira-shared-home  

