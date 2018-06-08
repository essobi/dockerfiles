FROM prettysmile/java8  
  
ENV TOMCAT_FILE_NAME apache-tomcat-7.0.59.tar.gz  
ENV TOMCAT_URL
https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.59/bin/apache-
tomcat-7.0.59.tar.gz  
ENV CATALINA_HOME /opt/apache-tomcat-7.0.59  
RUN apt-get update && apt-get -y install \  
unzip \  
net-tools \  
vim \  
iputils-ping \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget $TOMCAT_URL \  
&& tar xf $TOMCAT_FILE_NAME -C /opt \  
&& rm $TOMCAT_FILE_NAME  
  
COPY tomcat-users.xml $CATALINA_HOME/conf/  
COPY server.xml $CATALINA_HOME/conf/  
COPY setenv.sh $CATALINA_HOME/bin/  
  
EXPOSE 8080 8888  

