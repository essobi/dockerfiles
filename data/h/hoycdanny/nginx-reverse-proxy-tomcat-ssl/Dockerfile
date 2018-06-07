From tomcat:7.0-jre7  
MAINTAINER Danny,Ho <danny.ho@hpe.com>  
RUN $JAVA_HOME/bin/keytool -genkey -alias tomcat -keyalg RSA -storepass
changeit -keypass changeit -dname "CN=example.com,OU=,O=,L=,S=,C=SE"  
RUN sed -i 's/<Service name="Catalina">/<Service name="Catalina"> \n\n
<Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"\n
maxThreads="150" SSLEnabled="true" scheme="https" secure="true"\n
clientAuth="false" sslProtocol="TLS" \/>/' conf/server.xml  
RUN apt-get update && apt-get upgrade && apt-get -y install \  
curl \  
wget \  
git \  
vim \  
nginx \  
tomcat7 \  
software-properties-common  
RUN sed -i '42 i\location /tomcat { \  
proxy_pass https://127.0.0.1:8443/; \  
}' /etc/nginx/sites-available/default  
RUN sed -i '121 a\service nginx restart' /usr/local/tomcat/bin/catalina.sh  

