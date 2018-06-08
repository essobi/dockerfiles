FROM codenvy/jdk7  
RUN mkdir /home/user/tomcat8 && \  
wget -qO- "http://archive.apache.org/dist/tomcat/tomcat-8/v8.0.12/bin/apache-
tomcat-8.0.12.tar.gz" | tar -zx --strip-components=1 -C /home/user/tomcat8 &&
\  
rm -rf /home/user/tomcat8/webapps/*  
  
EXPOSE 8080  
WORKDIR /home/user/tomcat8/bin  
  
CMD ./catalina.sh run  

