FROM judekim/ubuntu-base-oracle-java:7  
ENV CONF_HOME /home/confluence  
ENV CONFLUENCE_VERSION 5.9.2  
ENV MYSQL_DRIVER_VERSION 5.1.38  
ENV LANG ko_KR.UTF-8  
RUN useradd --create-home --comment "Account for running Atlassian Confluence"
confluence \  
&& chmod -R a+rw ~confluence  
  
# download ``Atlassian Confluence`` standalone archive version  
RUN wget
"http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz" \  
&& tar -xzf "atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz" \  
&& rm "atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz" \  
&& mkdir -p "/usr/local/atlassian" \  
&& mv "atlassian-confluence-${CONFLUENCE_VERSION}"
"/usr/local/atlassian/confluence" \  
&& echo -e "\nconfluence.home=$CONF_HOME" >>
"/usr/local/atlassian/confluence/confluence/WEB-INF/classes/confluence-
init.properties" \  
&& chown -R confluence: "/usr/local/atlassian/confluence/temp" \  
&& chown -R confluence: "/usr/local/atlassian/confluence/logs" \  
&& chown -R confluence: "/usr/local/atlassian/confluence/work" \  
&& chmod -R 777 "/usr/local/atlassian/confluence/temp" \  
&& chmod -R 777 "/usr/local/atlassian/confluence/logs" \  
&& chmod -R 777 "/usr/local/atlassian/confluence/work" \  
&& wget "http://cdn.mysql.com/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& tar -xzf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& mv "mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar" "/usr/local/atlassian/confluence/lib/."
\  
&& rm -rf "mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
&& rm -rf "mysql-connector-java-${MYSQL_DRIVER_VERSION}" \  
&& chown confluence "/usr/local/atlassian/confluence/lib/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar"  
ADD server.xml /usr/local/atlassian/confluence/conf/server.xml  
  
# set the principal user as new non-root confluence account  
USER confluence  
  
# expose default ``Atlassian Confluence`` HTTP port  
EXPOSE 8090  
# set volume mount points for installation and home directory  
VOLUME ["/home/confluence", "/usr/local/atlassian/confluence"]  
  
# run ``Atlassian Confluence`` and as a foreground process by default  
ENTRYPOINT ["/usr/local/atlassian/confluence/bin/start-confluence.sh"]  
CMD ["-fg"]  

