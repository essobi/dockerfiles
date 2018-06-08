FROM fitpay/docker-java  
MAINTAINER Scott Stevelinck (scott@fit-pay.com)  
  
ENV UAA_CONFIG_PATH /uaa  
ENV CATALINA_HOME /tomcat  
  
ADD run.sh /tmp/  
ADD uaa.yml /uaa/uaa.yml  
RUN chmod +x /tmp/run.sh  
  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.68/bin/apache-
tomcat-7.0.68.tar.gz  
RUN wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.68/bin/apache-
tomcat-7.0.68.tar.gz.md5 | md5sum -c -  
  
RUN tar zxf apache-tomcat-7.0.68.tar.gz  
RUN rm apache-tomcat-7.0.68.tar.gz  
  
RUN mkdir /tomcat  
RUN mv apache-tomcat-7.0.68/* /tomcat  
RUN rm -rf /tomcat/webapps/*  
  
ADD cloudfoundry-identity-uaa-3.2.1.war /tomcat/webapps/ROOT.war  
ADD log4j.xml /log4j.xml  
  
VOLUME ["/uaa"]  
  
EXPOSE 8080  
CMD ["/tmp/run.sh"]  

