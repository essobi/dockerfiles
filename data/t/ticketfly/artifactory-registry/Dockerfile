FROM jfrog-docker-reg2.bintray.io/jfrog/artifactory-registry:4.16.1  
MAINTAINER Venkatesh Amudhan <venkatesh@ticketfly.com>  
  
RUN rpm --rebuilddb; yum install -y yum-plugin-ovl  
  
RUN yum install -y tar  
ADD http://cdn.mysql.com/Downloads/Connector-J/mysql-connector-
java-5.1.42.tar.gz /tmp/mysql-connector-java-5.1.42.tar.gz  
RUN cd /tmp; tar zxf mysql-connector-java-5.1.42.tar.gz; cp /tmp/mysql-
connector-java-5.1.42/mysql-connector-java-5.1.42-bin.jar
/var/opt/jfrog/artifactory/tomcat/lib  
  
RUN curl -L --cookie "gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u91-b14/jre-8u91-linux-x64.rpm" > jre-8u91-linux-x64.rpm; rpm -i
jre-8u91-linux-x64.rpm  
  
ADD https://download.newrelic.com/newrelic/java-agent/newrelic-
agent/3.38.0/newrelic-java-3.38.0.zip /tmp/newrelic.zip  
RUN yum install -y unzip && \  
unzip /tmp/newrelic.zip -d /opt/jfrog/artifactory/tomcat  
  
CMD java -jar /opt/jfrog/artifactory/tomcat/newrelic/newrelic.jar install && \  
chown -R artifactory: /opt/jfrog/artifactory/tomcat/newrelic && \  
/tmp/run.sh  

