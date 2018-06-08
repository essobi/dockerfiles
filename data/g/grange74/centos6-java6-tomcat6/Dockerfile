FROM grange74/centos6-java6  
MAINTAINER Nicolas Grange "grange74@gmail.com"  
# Download the latest Tomcat 6 and copy to /usr/local  
# The following commands are chained to keep the image size as small as
possible  
# It does unfortunately make it less readable so i try to explain each step:  
# 1. download/install tar  
# 2. download latest tomcat 6 from trusted mirror  
# 3. untar the tomcat6.tar.gz  
# 4. delete the tomcat6.tar.gz  
# 5 & 6\. Remove unnecessary webapps that come with Tomcat  
# 7. Move the tomcat6 folder to where we will run it from  
# 8. ask yum to clean itself up  
RUN yum -y install tar && \  
wget "http://apache.mirror.uber.com.au/tomcat/tomcat-6/v6.0.41/bin/apache-
tomcat-6.0.41.tar.gz" \  
-O /apache-tomcat-6.0.41.tar.gz && \  
tar xvzf /apache-tomcat-6.0.41.tar.gz && \  
rm /apache-tomcat-6.0.41.tar.gz && \  
rm -rf /apache-tomcat-6.0.41/webapps/docs && \  
rm -rf /apache-tomcat-6.0.41/webapps/examples && \  
mv /apache-tomcat-6.0.41/ /usr/local/ && \  
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
ADD tomcat-users.xml /usr/local/apache-tomcat-6.0.41/conf/tomcat-users.xml  
  
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
# Start Tomcat in the background  
ENV CATALINA_HOME /usr/local/apache-tomcat-6.0.41  
CMD exec ${CATALINA_HOME}/bin/catalina.sh run

