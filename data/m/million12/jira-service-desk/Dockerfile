FROM million12/centos-supervisor  
MAINTAINER Przemyslaw Ozgo linux@ozgo.info  
EXPOSE 8080  
# Supported DB: HSQL(default) and MySQL(MariaDB). to select MySQL use
DB_SUPPORT=mysql or DB_SUPPORT=mariadb on docekr run.  
ENV JIRASD_VERSION=3.1.0 \  
JIRA_VERSION=7.1.0 \  
DB_SUPPORT=default  
  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y java-1.8.0-openjdk tar mariadb && \  
yum clean all && \  
curl -L https://www.atlassian.com/software/jira/downloads/binary/atlassian-
servicedesk-${JIRASD_VERSION}-jira-${JIRA_VERSION}-x64.bin -o /tmp/jira.bin &&
\  
chmod +x /tmp/jira.bin && \  
curl -L http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.37.tar.gz -o /tmp/mysql-connector-java-5.1.37.tar.gz  
  
COPY container-files/ /  

