FROM judekim/ubuntu-base-oracle-java:8  
ENV JIRA_HOME /home/jira  
ENV JIRA_VERSION 7.0.4  
ENV MYSQL_DRIVER_VERSION 5.1.38  
ENV CATALINA_OPTS -Xms128m -Xmx1024m  
  
# create non-root user to run ``Atlassian Jira``  
RUN useradd --create-home --comment "Account for running Atlassian Jira" jira
\  
&& chmod -R a+rw ~jira  
  
# download ``Atlassian Jira`` standalone archive version  
# changed download link -
https://downloads.atlassian.com/software/jira/downloads/atlassian-jira-
software-7.0.4-jira-7.0.4.tar.gz  
RUN wget "https://downloads.atlassian.com/software/jira/downloads/atlassian-
jira-software-${JIRA_VERSION}-jira-${JIRA_VERSION}.tar.gz" \  
&& tar -xzf "atlassian-jira-
software-${JIRA_VERSION}-jira-${JIRA_VERSION}.tar.gz" \  
&& rm -rf "atlassian-jira-
software-${JIRA_VERSION}-jira-${JIRA_VERSION}.tar.gz" \  
&& mkdir -p "/usr/local/atlassian" \  
&& mv "atlassian-jira-software-${JIRA_VERSION}-standalone"
"/usr/local/atlassian/jira" \  
&& echo -e "\njira.home=$JIRA_HOME" >> "/usr/local/atlassian/jira/atlassian-
jira/WEB-INF/classes/jira-application.properties" \  
&& chown -R jira: "/usr/local/atlassian/jira/temp" \  
&& chown -R jira: "/usr/local/atlassian/jira/logs" \  
&& chown -R jira: "/usr/local/atlassian/jira/work" \  
&& chmod -R 777 "/usr/local/atlassian/jira/temp" \  
&& chmod -R 777 "/usr/local/atlassian/jira/logs" \  
&& chmod -R 777 "/usr/local/atlassian/jira/work" \  
&& wget "http://cdn.mysql.com/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& tar -xzf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& mv "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" "/usr/local/atlassian/jira/lib/." \  
&& rm -rf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& rm -rf "mysql-connector-java-${MYSQL_DRIVER_VERSION}" \  
&& chown jira "/usr/local/atlassian/jira/lib/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar"  
# set the current user as ``jira`` since starting the server would execute as
current user  
USER jira  
  
# expose default HTTP connector port  
EXPOSE 8080  
# set volume mount points for installation and home directory  
VOLUME ["/home/jira", "/usr/local/atlassian/jira"]  
  
# run ``Atlassian Jira`` and as a foreground process by default  
ENTRYPOINT ["/usr/local/atlassian/jira/bin/start-jira.sh"]  
CMD ["-fg"]  

