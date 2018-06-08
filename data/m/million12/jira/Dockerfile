FROM million12/centos-supervisor  
MAINTAINER Przemyslaw Ozgo linux@ozgo.info  
  
# Supported DB: HSQL(default) and MySQL(MariaDB). to select MySQL use
DB_SUPPORT=mysql or DB_SUPPORT=mariadb on docekr run.  
ENV DB_SUPPORT=default \  
JIRA_VERSION=7.0.0  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y java-1.8.0-openjdk tar mariadb && \  
yum clean all && \  
curl -L https://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-software-${JIRA_VERSION}-jira-${JIRA_VERSION}-x64.bin -o /tmp/jira.bin &&
\  
chmod +x /tmp/jira.bin  
  
ADD container-files/ /  

