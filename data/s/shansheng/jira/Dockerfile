  
#  
# author: sheng (mailto:shanshengsheng@gmail.com)  
#  
  
FROM shansheng/jdk:8  
# LABEL maintainer="shanshengsheng@gmail.com" \  
# provider="SSS, Ltd."  
  
ENV JIRA_VERSION=7.4.3 \  
JIRA_APP=/opt/jira-7.4.3 \  
JIRA_HOME=/opt/jira_home \  
JIRA_PORT=8080 \  
JAVA_VM_MEM_MIN=512 \  
JAVA_VM_MEM_MAX=1024 \  
MYSQL_DATABASE=jira \  
MYSQL_USER=jira \  
MYSQL_PASSWORD=jira \  
MYSQL_HOST=mysql \  
MYSQL_PORT=3306 \  
# YES|yes|y NO|no|n  
MANUAL_CONFIG_DATABASE=NO  
  
VOLUME ${JIRA_HOME}  
  
EXPOSE ${JIRA_PORT}  
  
# .tar, .tar.gz  
# ADD resources/jira.tar* /opt/  
ADD resources/*.jar /opt/  
  
RUN curl --fail --location --retry 3 \  
https://downloads.atlassian.com/software/jira/downloads/atlassian-jira-
software-7.4.3.tar.gz \  
-o /tmp/jira.tar.gz \  
&& tar -zxf /tmp/jira.tar.gz -C /opt/ \  
&& \mv -f /opt/atlassian-jira-software-* ${JIRA_APP} \  
&& \rm -f /tmp/jira.tar.gz \  
&& curl --fail --location --retry 3
http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.43/mysql-
connector-java-5.1.43.jar \  
-o ${JIRA_APP}/lib/mysql-connector-java-5.1.43.jar \  
&& \cp -r /opt/atlassian-extras-3.1.2.jar ${JIRA_APP}/lib \  
&& \cp -r /opt/atlassian-extras-3.2.jar ${JIRA_APP}/lib  
# https://confluence.atlassian.com/adminjiraserver073/connecting-jira-
applications-to-mysql-861253043.html  
ADD resources/dbconfig.xml ${JIRA_APP}/templates/dbconfig.xml  
  
ADD resources/entrypoint.sh /opt/entrypoint.sh  
  
RUN chmod +x /opt/entrypoint.sh  
  
ENTRYPOINT [ "/bin/sh", "-c", "/opt/entrypoint.sh" ]  

