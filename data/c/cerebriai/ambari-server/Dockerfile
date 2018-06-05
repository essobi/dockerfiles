FROM hortonworks/ambari-base:7.2-v7  
MAINTAINER Hortonworks  
  
# add ambari repo  
#ADD ambari.repo /etc/yum.repos.d/  
RUN wget -nv http://public-
repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.5.0.3/ambari.repo -O
/etc/yum.repos.d/ambari.repo  
  
# initscripts (service wrapper for servicectl) is need othewise the Ambari is
unable to start postgresql  
#RUN yum update -y  
RUN yum install -y ambari-server sudo && yum clean all  
  
# add ambari shell to the image so new users don't need the 1GB java image  
RUN curl -o /tmp/ambari-shell.jar https://s3-eu-
west-1.amazonaws.com/maven.sequenceiq.com/releases/com/sequenceiq/ambari-
shell/0.1.25/ambari-shell-0.1.25.jar  
ADD shell/install-cluster.sh /tmp/  
ADD shell/wait-for-host-number.sh /tmp/  
ADD shell/ambari-shell.sh /tmp/  
  
ENV PLUGIN_PATH /plugins  
WORKDIR /tmp  
  
ADD init/init-server.sh /opt/ambari-server/init-server.sh  
RUN chmod u+x /opt/ambari-server/init-server.sh  
  
# add mysql and psql connectors to ambari-server so it can be downloaded by
services (e.g.: Ranger)  
ADD http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.39.tar.gz /var/lib/ambari-server/resources/mysql-jdbc-driver.jar  
ADD https://jdbc.postgresql.org/download/postgresql-9.4.1208.jre7.jar
/var/lib/ambari-server/resources/postgres-jdbc-driver.jar  
  
ADD init/ambari-server.service /etc/systemd/system/ambari-server.service  
  
# Install Solr Service  
COPY solr-service-mpack-5.5.2.2.5.tar.gz /tmp/solr-service-
mpack-5.5.2.2.5.tar.gz  
RUN ambari-server install-mpack --mpack=/tmp/solr-service-
mpack-5.5.2.2.5.tar.gz -v  
  
RUN systemctl enable ambari-server  
  
RUN echo DefaultEnvironment=\"JAVA_HOME=$JAVA_HOME\" >>
/etc/systemd/system.conf  
  
EXPOSE 8080  

