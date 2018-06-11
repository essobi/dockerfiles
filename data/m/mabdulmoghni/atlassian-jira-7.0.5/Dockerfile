FROM ubuntu:14.04  
MAINTAINER Mohamed Abdulmoghni <mabdulmoghni@cloud9ers.com>  
############################################################  
############## update Image ################################  
### Ensure up to date system  
### Clean up APT when done  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get --quiet update && \  
apt-get --quiet --yes --force-yes upgrade && apt-get -y install wget tar && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
###############################################################  
# Configuration variables.  
ENV JIRA_HOME /home/jira/jira_home  
ENV JIRA_INSTALL /home/jira/atlassian  
ENV JIRA_VERSION 7.0.5  
ENV CONNECTOR mysql-connector-java-5.1.38  
################################################################  
RUN /usr/sbin/useradd --home-dir /home/jira --shell /bin/bash jira  
WORKDIR /home/jira  
RUN wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-software-${JIRA_VERSION}-jira-${JIRA_VERSION}-x64.bin && \  
chmod +x atlassian-jira-software-${JIRA_VERSION}-jira-${JIRA_VERSION}-x64.bin  
###uploading response.varfile to perform unattended express jira installation
and accept defaults###  
ADD ./response.varfile /home/jira/response.varfile  
RUN chown -R jira:jira /home/jira  
USER jira  
RUN sh atlassian-jira-software-${JIRA_VERSION}-jira-${JIRA_VERSION}-x64.bin -q
-varfile response.varfile && \  
rm -f atlassian-jira-software-${JIRA_VERSION}-jira-${JIRA_VERSION}-x64.bin &&
\  
/bin/bash -c 'echo -e "\n jira.home=$JIRA_HOME" >>
"${JIRA_INSTALL}/jira/atlassian-jira/WEB-INF/classes/jira-
application.properties"'  
EXPOSE 8080  
###install mysql-connector-java###  
RUN wget http://dev.mysql.com/get/Downloads/Connector-J/${CONNECTOR}.tar.gz &&
\  
tar xzf ${CONNECTOR}.tar.gz && mv ${CONNECTOR}/${CONNECTOR}-bin.jar
${JIRA_INSTALL}/jira/lib/  
VOLUME ["/home/jira/jira_home"]  
WORKDIR ${JIRA_HOME}  
# Run Atlassian JIRA as a foreground process by default.  
ENTRYPOINT ["/home/jira/atlassian/jira/bin/start-jira.sh", "-fg"]  

