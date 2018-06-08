FROM rodrigosaito/java7  
  
MAINTAINER Rodrigo Saito <rodrigo.saito@gmail.com>  
  
WORKDIR /opt  
  
RUN wget http://www.us.apache.org/dist/tomcat/tomcat-7/v7.0.54/bin/apache-
tomcat-7.0.54.tar.gz  
RUN tar xzvf apache-tomcat-7.0.54.tar.gz  
RUN ln -s apache-tomcat-7.0.54 tomcat  
  
ENTRYPOINT [ "/opt/tomcat/bin/catalina.sh", "run" ]  
  

