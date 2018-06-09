FROM openjdk:8  
MAINTAINER Swapnali Pingale <yeole.swapnali@gmail.com>  
  
ENV HOME /root  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV JIRA_HOME /var/atlassian/application-data/jira  
ENV JIRA_INSTALL_DIR /opt/atlassian/jira  
ENV JIRA_VERSION 7.3.6  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends -t jessie-backports
libtcnative-1 \  
&& apt-get clean \  
&& mkdir -p "${JIRA_HOME}" \  
&& mkdir -p "${JIRA_HOME}/caches/indexes" \  
&& chmod -R 700 "${JIRA_HOME}" \  
&& mkdir -p "${JIRA_INSTALL_DIR}/conf/Catalina" \  
&& curl -Ls
"https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-
core-${JIRA_VERSION}.tar.gz" | tar -xz --directory "${JIRA_INSTALL_DIR}"
\--strip-components=1 --no-same-owner \  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.34.tar.gz" | tar -xz --directory "${JIRA_INSTALL_DIR}/lib" \--strip-
components=1 --no-same-owner "mysql-connector-java-5.1.34/mysql-connector-
java-5.1.34-bin.jar" \  
&& sed --in-place "s/java version/openjdk version/g"
"${JIRA_INSTALL_DIR}/bin/check-java.sh" \  
&& echo -e "\njira.home=$JIRA_HOME" >> "${JIRA_INSTALL_DIR}/atlassian-
jira/WEB-INF/classes/jira-application.properties" \  
&& touch -d "@0" "${JIRA_INSTALL_DIR}/conf/server.xml"  
  
VOLUME ["/var/atlassian/application-data/jira", "/opt/atlassian/jira/logs"]  
WORKDIR /opt/atlassian/jira  
  
CMD ["/opt/atlassian/jira/bin/start-jira.sh", "run"]  
  
EXPOSE 8080  
ENV MYSQL_USER root  
ENV MYSQL_PASS root  
  
RUN echo "mysql-server mysql-server/root_password password root" | debconf-
set-selections  
RUN echo "mysql-server mysql-server/root_password_again password root" |
debconf-set-selections  
  
RUN apt-get install -y mysql-server  
  
RUN rm -rf /var/lib/mysql/*  
  
ADD build/my.cnf /etc/mysql/my.cnf  
ADD build/dbconfig.xml /var/atlassian/application-data/jira  
  
RUN mkdir /etc/mysql/run  
ADD runit/mysql.sh /etc/mysql/run  
RUN chmod +x /etc/mysql/run  
  
ADD build/setup /root/setup  
  
ADD my_init.d/99_mysql_setup.sh /etc/my_init.d/99_mysql_setup.sh  
RUN chmod +x /etc/my_init.d/99_mysql_setup.sh  
  
EXPOSE 3306  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

