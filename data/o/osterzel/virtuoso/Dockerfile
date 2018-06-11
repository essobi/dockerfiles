# docker build -t vitraux .  
# docker run -d -p 8080:8080 --name test_vitraux vitraux  
FROM centos:6.7  
MAINTAINER TDCS Frameworks <adrian.chan@homeoffice.gsi.gov.uk>  
ENV VITRAUX_VIRTUOSO_VERSION 1.4.6  
# Requires access to the follow URLs -  
# http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-
maven.repo  
# http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.38.tar.gz  
#
https://gitlab.com/tdcs_framework/maven/raw/master/repository/uk/gov/homeoffice/vitraux/virtuoso/$VITRAUX_VIRTUOSO_VERSION/database/database.sql  
#
https://gitlab.com/tdcs_framework/maven/raw/master/repository/uk/gov/homeoffice/vitraux/virtuoso/$VITRAUX_VIRTUOSO_VERSION/virtuoso-$VITRAUX_VIRTUOSO_VERSION.war  
# Requires the following packages -  
# unzip  
# zip  
# apache-maven (repo added above)  
# java-1.8.0-openjdk  
# java-1.8.0-openjdk-devel  
# tomcat6.x86_64  
# mysql-server.x86_64  
# Update image and install wget  
RUN yum -y update && yum clean all && yum install wget -y  
  
# Add apache-maven repository  
RUN wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-
maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo  
  
# Install dependencies  
RUN yum install unzip -y \  
zip \  
apache-maven \  
java-1.8.0-openjdk \  
java-1.8.0-openjdk-devel \  
tomcat6.x86_64 \  
mysql-server.x86_64  
  
# Add additional vitraux directories  
RUN mkdir -p /var/data/log/virtuoso && chown -R tomcat.tomcat
/var/data/log/virtuoso \  
&& mkdir -p /var/data/virtuoso && chown -R tomcat.tomcat /var/data/virtuoso \  
&& mkdir /usr/share/tomcat6/webapps/results && chown -R tomcat.tomcat
/usr/share/tomcat6/webapps/results  
  
# Add a shell for the tomcat user  
# Required for maven repository as tomcat will execute jobs  
RUN mkdir /home/tomcat && chown -R tomcat.tomcat /home/tomcat \  
&& usermod -d /home/tomcat tomcat \  
&& usermod -s /bin/bash tomcat  
  
# Configure Java8  
RUN update-alternatives --set java
/usr/lib/jvm/jre-1.8.0-openjdk.x86_64/bin/java \  
&& update-alternatives --set javac
/usr/lib/jvm/java-1.8.0-openjdk.x86_64/bin/javac \  
&& echo 'setenv JAVA_HOME /usr/lib/jvm/jre-1.8.0-openjdk.x86_64' >
/etc/profile.d/java.csh \  
&& printf '%s\n' 'JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk.x86_64' 'export
JAVA_HOME' > /etc/profile.d/java.sh  
  
# Add MySQL JDBC driver  
RUN wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.38.tar.gz \  
&& tar xvf mysql-connector-java-5.1.38.tar.gz \  
&& cp mysql-connector-java-5.1.38/mysql-connector-java-5.1.38-bin.jar
/usr/share/tomcat6/lib/ \  
&& rm -rf mysql-connector-java-5.1.38  
  
# Install MySQL and create Vitraux database  
RUN wget
https://gitlab.com/tdcs_framework/maven/raw/master/repository/uk/gov/homeoffice/vitraux/virtuoso/$VITRAUX_VIRTUOSO_VERSION/database/database.sql
-O /tmp/database.sql \  
&& printf '%s\n' '#!/bin/bash' 'service mysqld start' 'mysqladmin -u root
password admin' 'mysql --user=root --password=admin < /tmp/database.sql' >
/tmp/configure_db.sh \  
&& chmod +x /tmp/configure_db.sh \  
&& . /tmp/configure_db.sh  
  
# Install Vitraux-Virtuoso  
RUN wget
https://gitlab.com/tdcs_framework/maven/raw/master/repository/uk/gov/homeoffice/vitraux/virtuoso/$VITRAUX_VIRTUOSO_VERSION/virtuoso-$VITRAUX_VIRTUOSO_VERSION.war
-O /usr/share/tomcat6/webapps/virtuoso.war  
  
# Open port 8080 for tomcat  
EXPOSE 8080  
# Create startup script and server.log to tail  
RUN printf '%s\n' '#!/bin/bash' 'service tomcat6 start' 'service mysqld start'
> /tmp/init_vitraux.sh \  
&& chmod +x /tmp/init_vitraux.sh \  
&& touch /var/data/log/virtuoso/server.log \  
&& chown tomcat.tomcat /var/data/log/virtuoso/server.log  
  
# Start tomcat6 and mysqld via script  
CMD /tmp/init_vitraux.sh && tail -f /var/data/log/virtuoso/server.log  

