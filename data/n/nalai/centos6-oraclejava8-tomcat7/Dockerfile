FROM nalai/centos6-oraclejava8  
MAINTAINER Nathaniel Lai "nathaniel.lai@retrievercommunications.com"  
#Install Tomcat 7  
#Download the latest Tomcat 7 and copy to /usr/local  
RUN yum -y install tar  
RUN wget "http://apache.mirror.uber.com.au/tomcat/tomcat-7/v7.0.57/bin/apache-
tomcat-7.0.57.tar.gz" \  
-O /apache-tomcat-7.0.57.tar.gz && \  
tar xvzf /apache-tomcat-7.0.57.tar.gz && \  
rm /apache-tomcat-7.0.57.tar.gz && \  
rm -rf /apache-tomcat-7.0.57/webapps/docs && \  
rm -rf /apache-tomcat-7.0.57/webapps/examples && \  
mv /apache-tomcat-7.0.57/ /usr/local/ && \  
yum clean all  
  
# Need this to avoid the following message:  
# The APR based Apache Tomcat Native library which allows optimal performance
in  
# production environments was not found on the java.library.path  
# This step will give warnings but they don't seem to cause any problems  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm && \  
yum -y install tomcat-native && \  
yum clean all  
  
# Overwrite the default to set a user/password for Tomcat manager  
ADD tomcat-users.xml /usr/local/apache-tomcat-7.0.57/conf/tomcat-users.xml  
  
# TODO enable SSL by creating a key, moving it to right tomcat location and
edit server.xml  
# RUN keytool -genkey -alias tomcat -keyalg RSA  
# RUN mv /root/.keystore /usr/share/tomcat6/  
# <Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true"  
# maxThreads="150" scheme="https" secure="true"  
# clientAuth="false" sslProtocol="TLS" />  
#EXPOSE 8443  
# Expose the standard Tomcat ports  
EXPOSE 8080

