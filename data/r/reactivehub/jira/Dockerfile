FROM java:7-jre  
  
ENV JIRA_VERSION 6.3.15  
ENV JIRA_DOWNLOAD_URL
http://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-$JIRA_VERSION.tar.gz  
  
RUN set -x \  
&& mkdir -p /opt/jira \  
&& mkdir -p /home/jira \  
&& ( curl -sSL $JIRA_DOWNLOAD_URL | tar -xzf - -C /opt/jira --strip-
components=1 ) \  
&& sed -i "s:jira.home =:jira.home=/home/jira:g" /opt/jira/atlassian-jira/WEB-
INF/classes/jira-application.properties  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
VOLUME /home/jira  
  
EXPOSE 8080  
WORKDIR /home/jira  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["jira"]  

