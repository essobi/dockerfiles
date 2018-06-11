FROM tomcat:9.0  
MAINTAINER Jackliu <jackl3@cisco.com>  
RUN apt-get update && apt-get install -y vim  
RUN mkdir -p /usr/local/tomcat/webapps/helloworld  
COPY helloworld /usr/local/tomcat/webapps/helloworld  
RUN mv /usr/local/tomcat/conf/server.xml /usr/local/tomcat/conf/server.xml.bak  
COPY server.xml /usr/local/tomcat/conf/server.xml  
RUN keytool -genkey -alias tomcat -keyalg RSA -storepass IdKomucFad1 -keypass
IdKomucFad1 -dname CN=qa,OU=tropo,O=cisco,L=bj,ST=bj,C=cn  
VOLUME /usr/local/tomcat/webapps  
WORKDIR /usr/local/tomcat/bin  
EXPOSE 8080 8443  
CMD ["catalina.sh", "run"]  

