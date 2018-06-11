FROM openjdk:6  
WORKDIR /app  
  
RUN wget -O /app/jod-tomcat.zip
'http://sourceforge.net/projects/jodconverter/files/JODConverter/2.2.2/jodconverter-
tomcat-2.2.2.zip/download' && \  
unzip jod-tomcat.zip  
  
ADD ./applicationContext.xml /app/jodconverter-
tomcat-2.2.2/webapps/converter/WEB-INF/applicationContext.xml  
  
CMD bash jodconverter-tomcat-2.2.2/bin/catalina.sh run  

