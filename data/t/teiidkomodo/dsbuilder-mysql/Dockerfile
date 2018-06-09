#  
# Docker image configuration for dsbuilder configured with a locally available  
# mysql database and driver added to wildfly.  
#  
FROM teiidkomodo/dsbuilder:vanilla-1.0  
MAINTAINER Teiid-Komodo Community <http://teiiddesigner.jboss.org>  
  
#  
# Env variables  
#  
ENV BIN_DIR /usr/local/bin  
ENV JBOSS_HOME /opt/jboss/wildfly  
ENV MYSQL_ROOT_PASS secret  
ENV MYSQL_USER_PASS admin  
ENV MYSQL_CONNECTOR mysql-connector-java-5.1.40  
#  
# Change to root user  
#  
USER root  
  
#  
# Copy wildfly exec script and set permissions  
#  
COPY wildfly-exec.sh ${BIN_DIR}/  
RUN chmod +x ${BIN_DIR}/wildfly-exec.sh  
  
#  
# Add the mysql connector driver to wildfly  
#  
ADD https://dev.mysql.com/get/Downloads/Connector-J/${MYSQL_CONNECTOR}.zip
${JBOSS_HOME}  
RUN unzip ${JBOSS_HOME}/${MYSQL_CONNECTOR}.zip
${MYSQL_CONNECTOR}/${MYSQL_CONNECTOR}-bin.jar -d ${JBOSS_HOME} && \  
mv ${JBOSS_HOME}/${MYSQL_CONNECTOR}/${MYSQL_CONNECTOR}-bin.jar
${JBOSS_HOME}/standalone/deployments/mysql-connector-java-bin.jar && \  
touch ${JBOSS_HOME}/standalone/deployments/mysql-connector-java-
bin.jar.dodeploy && \  
rm -rf ${JBOSS_HOME}/${MYSQL_CONNECTOR}*  
  
#  
# ADD and COPY always create files as root. Need to call  
# chown to have them owned by the jboss user  
#  
RUN chown -R jboss:jboss ${JBOSS_HOME}/standalone  
  
#  
# Install mysql-server using yum  
#  
ADD http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm /tmp  
RUN rpm -ivh /tmp/mysql-community-release-el7-5.noarch.rpm  
RUN yum -y install --setopt=tsflags=nodocs epel-release && \  
yum -y install --setopt=tsflags=nodocs mysql-server mysql pwgen supervisor
bash-completion psmisc net-tools && \  
yum -y update && yum clean all  
  
#  
# Copy mysql exec script and set permissions  
#  
COPY mysql-exec.sh ${BIN_DIR}/  
RUN chmod +x ${BIN_DIR}/mysql-exec.sh  
  
#  
# Copy mysql additional options to /etc  
#  
COPY etc/my.cnf.d/* /etc/my.cnf.d/  
  
#  
# Expose the mysql port, which should be in addition to the wildfly ports  
#  
EXPOSE 3306  
#  
# The default cmd for this container  
#  
CMD ["/bin/sh", "-c", "${BIN_DIR}/mysql-exec.sh && ${BIN_DIR}/wildfly-
exec.sh"]  

