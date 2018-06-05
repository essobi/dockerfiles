#  
# TeamCity 9.1.3 server running on 32bit VM and using Postgres JDBC  
#  
FROM ubuntu:trusty  
MAINTAINER Uri Savelchev <alterrebe@gmail.com>  
EXPOSE 8080  
VOLUME /teamcity  
  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8 locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
# Initialize Ubuntu package system  
RUN apt-get update -qq && apt-get install -y -qq htop wget  
  
# Install Java8 32bit. Unfortunately we can't use webupd8 PPA for the purpose  
ENV JDK_HOME /jdk1.8.0_60  
  
RUN dpkg --add-architecture i386 && \  
apt-get update -qq && \  
apt-get install -y -qq libc6:i386 && \  
wget -O jdk.tar.gz -q --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/8u60-b27/jdk-8u60-linux-i586.tar.gz && \  
tar xzf jdk.tar.gz && \  
rm -f jdk.tar.gz ${JDK_HOME}/src.zip ${JDK_HOME}/javafx-src.zip && \  
update-alternatives --install /usr/bin/java java ${JDK_HOME}/bin/java 100  
  
# Install Tomcat7 (borrowed from tutum/tomcat image). The 7.0.59 is the
version recommended by JetBrains.  
ENV TOMCAT_MAJOR_VERSION 7  
ENV TOMCAT_MINOR_VERSION 7.0.59  
ENV CATALINA_HOME /tomcat  
  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* tomcat  
  
# Install Tomcat Native Library. The standard repo contains an old version,
use a custom PPA  
RUN echo "deb http://ppa.launchpad.net/pharmgkb/trusty/ubuntu trusty main" >
/etc/apt/sources.list.d/tcnative.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9BF906AAB16AA3F1 && \  
apt-get update -qq && \  
apt-get install -y -qq libtcnative-1:i386  
  
ENV CATALINA_OPTS -Xmx1200m -XX:MaxPermSize=270m
-Djava.library.path=/lib/i386-linux-gnu:/usr/lib/i386-linux-gnu  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  
  
# Now install TeamCity and Postgres JDBC driver (TeamCity needs jdbc41)  
ENV TEAMCITY_DATA_PATH /teamcity  
RUN rm -rf ${CATALINA_HOME}/webapps/* && \  
wget -q -O ${CATALINA_HOME}/webapps/ROOT.war http://download-
cf.jetbrains.com/teamcity/TeamCity-9.1.3.war && \  
wget -q -O ${CATALINA_HOME}/lib/postgresql-9.4-1203.jdbc41.jar
https://jdbc.postgresql.org/download/postgresql-9.4-1203.jdbc41.jar  
  

