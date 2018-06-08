# Centos based container with Java, Tomcat and Magnolia CMS Core  
#FROM centos:centos7  
# Ubuntu based container with Java, Tomcat and Magnolia CMS Core  
FROM ubuntu:trusty  
MAINTAINER Swamy Kottur  
  
# Prepare Database environment  
# ENV MYSQL_JDBC_PACKAGE mysql-connector-java-5.1.36  
# ENV POSTGRESQL_JDBC_PACKAGE postgresql-9.4-1201.jdbc41  
# Install prepare infrastructure  
RUN apt -y update && \  
apt -y install wget && \  
apt -y install tar  
  
# Prepare environment  
ENV JAVA_HOME /opt/java  
ENV JRE_HOME /opt/java/jre  
ENV CATALINA_HOME /opt/tomcat  
ENV CATALINA_TMPDIR /tmp/tomcat  
ENV PATH
$PATH:$JAVA_HOME/bin:$JRE_HOME/bin:$CATALINA_HOME/bin:$CATALINA_HOME/scripts  
  
# Install Oracle Java8  
ENV JAVA_VERSION 8u131  
ENV JAVA_BUILD b11  
  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}-${JAVA_BUILD}/d54c1d3a095b4ff2b6607d096fa80163/jdk-${JAVA_VERSION}-linux-x64.tar.gz"
&& \  
tar -xzf jdk-${JAVA_VERSION}-linux-x64.tar.gz && \  
rm jdk*.tar.gz && \  
mv jdk* ${JAVA_HOME}  
  
RUN update-alternatives --install /usr/bin/java java /opt/java/bin/java 2 && \  
update-alternatives --install /usr/bin/jar jar /opt/java/bin/jar 2 && \  
update-alternatives --install /usr/bin/javac javac /opt/java/bin/javac 2 && \  
update-alternatives --set jar /opt/java/bin/jar && \  
update-alternatives --set javac /opt/java/bin/javac  
  
# Install Tomcat  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.5.20  
RUN wget
https://www.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz && \  
tar -xvf apache-tomcat-${TOMCAT_VERSION}.tar.gz && \  
rm apache-tomcat*.tar.gz && \  
mv apache-tomcat* ${CATALINA_HOME}  
  
RUN chmod +x ${CATALINA_HOME}/bin/*sh  
  
# Make sure that the temporary directory exists  
RUN mkdir -p $CATALINA_TMPDIR  
  
# Remove all webapps from the default Tomcat installation  
RUN rm -rf $CATALINA_HOME/webapps/*  
  
# Copy tomcat configuration files from the project to the container  
# COPY tomcat/setenv.sh $CATALINA_HOME/bin/setenv.sh  
# Install JDBC drivers  
# RUN mkdir $CATALINA_HOME/lib/jdbc  
# RUN wget -nv
http://jdbc.postgresql.org/download/$POSTGRESQL_JDBC_PACKAGE.jar -O
$CATALINA_HOME/lib/$POSTGRESQL_JDBC_PACKAGE.jar  
# RUN wget -nv -O -
http://dev.mysql.com/get/Downloads/Connector-J/$MYSQL_JDBC_PACKAGE.tar.gz |
tar -C /tmp -xvzf - $MYSQL_JDBC_PACKAGE/$MYSQL_JDBC_PACKAGE-bin.jar  
# RUN mv /tmp/$MYSQL_JDBC_PACKAGE/$MYSQL_JDBC_PACKAGE-bin.jar
$CATALINA_HOME/lib  
# ADD
https://sourceforge.net/projects/magnolia/files/magnolia/Magnolia%20CE%205.5.4/magnolia-
community-demo-webapp-5.5.4.war/download?use_mirror=autoselect
$CATALINA_HOME/webapps/ROOT.war  
# ADD
https://sourceforge.net/projects/magnolia/files/magnolia/Magnolia%20CE%205.5.4/magnolia-
community-demo-webapp-5.5.4.war/download?use_mirror=autoselect
$CATALINA_HOME/webapps/ROOT.war  
# COPY jetblue-cms-webapp/target/jetblue-cms-webapp-1.0-SNAPSHOT.war
$CATALINA_HOME/webapps/ROOT.war  
# Start the tomcat instance  
ENTRYPOINT ["/opt/tomcat/bin/catalina.sh", "run"]  
CMD [""]  
  
# Expose the ports  
EXPOSE 8080

