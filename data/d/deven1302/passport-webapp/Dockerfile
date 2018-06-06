  
FROM tomcat:8.0-jre8  
  
MAINTAINER "Devendra <dev_nalawade@yahoo.com>"  
RUN apt-get update && apt-get install -y --no-install-recommends  
  
ENV PATH=$PATH:$JRE_HOME/bin  
  
RUN mkdir -p "/etc/cas/config"  
  
RUN mkdir -p "/usr/local/tomcat/conf/keys"  
  
RUN [ ! -f /usr/local/tomcat/conf/keys/keystore ] \  
&& printf
tomcat_admin\\\ntomcat_admin\\\n\\\n\\\n\\\n\\\n\\\n\\\ny\\\ntomcat_admin\\\ntomcat_admin\\\n
| keytool -genkey -alias tomcat -keyalg RSA -keystore
/usr/local/tomcat/conf/keys/keystore;  
  
RUN cp -f /usr/local/tomcat/conf/keys/keystore /etc/cas/config/keystore  
ADD "conf/server.xml" "/usr/local/tomcat/conf/"  
ADD "etc/cas/config" "/etc/cas/config"  
  
ADD "war/cas.war" "/usr/local/tomcat/webapps/passport.war"  
VOLUME ["/etc/cas/config", "/usr/local/tomcat/webapps/"]  
  
EXPOSE 8080  
EXPOSE 8443  

