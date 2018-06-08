############################################################  
#Dockerfile to build Liferay Community Edition Portal 7.0.3 GA4 (Wilberforce /
Build 7003 / June 19, 2017). Based on CentOS Latest#  
############################################################  
  
# Set the base image to centos  
FROM centos:latest  
  
MAINTAINER felixcentmerino.wordpress.com  
  
# Update the repository sources list  
RUN yum update -y && yum install -y unzip && yum install -y wget && yum
install -y telnet  
  
# Install java8 jdk && Tunning java  
RUN yum install -y wget && \  
wget \  
\--no-cookies \  
\--no-check-certificate \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm"
&& \  
yum localinstall -y "jdk-8u131-linux-x64.rpm" && \  
rm -f "jdk-8u131-linux-x64.rpm" && \  
update-alternatives --install "/usr/bin/java" "java"
"/usr/java/latest/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"/usr/java/latest/bin/javaws" 1 && \  
update-alternatives --install "/usr/bin/javac" "javac"
"/usr/java/latest/bin/javac" 1 && \  
sed -i "s/file:\/dev\/random/file:\/dev\/\\.\/urandom/g"
/usr/java/jdk1.8.0_131/jre/lib/security/java.security  
  
# Download and install liferay  
  
RUN curl -OL
https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.0.3%20GA4/liferay-
ce-portal-tomcat-7.0-ga4-20170613175008905.zip && \  
unzip liferay-ce-portal-tomcat-7.0-ga4-20170613175008905.zip -d /opt && \  
rm liferay-ce-portal-tomcat-7.0-ga4-20170613175008905.zip && \  
ln -s /opt/liferay-ce-portal-7.0-ga4 /opt/liferay-portal && \  
ln -s /opt/liferay-portal/tomcat-8.0.32 /opt/liferay-portal/tomcat  
  
# Add configuration files  
ADD resources/portal-ext.properties /opt/liferay-
portal/tomcat/webapps/ROOT/WEB-INF/classes/portal-ext.properties  
ADD resources/portal-setup-wizard.properties /opt/liferay-portal/portal-setup-
wizard.properties  
ADD resources/setenv.sh /opt/liferay-portal/tomcat/bin/setenv.sh  
ADD resources/server.xml /opt/liferay-portal/tomcat/conf  
ADD resources/mysql-connector-java-5.1.39-bin.jar /opt/liferay-
portal/tomcat/lib/ext/mysql-connector-java-5.1.39-bin.jar  
  
# Expose port 8080  
EXPOSE 8080  
  
# Create user and change permissions  
RUN groupadd -r Adminweb && \  
useradd -r -u 999 -g Adminweb -d /home/Adminwas -ms /bin/bash Adminwas && \  
chown Adminwas:Adminweb -R /opt && \  
echo "root:Docker!" | chpasswd  
  
#Change user  
USER 999  
ENV PATH=$PATH:/opt/liferay-portal/tomcat/bin  
  
CMD ["catalina.sh", "run"]  

