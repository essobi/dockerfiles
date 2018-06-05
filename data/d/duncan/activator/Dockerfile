FROM duncan/java  
MAINTAINER James Duncan Davidson <duncan@jdd.io>  
  
RUN cd /opt && \  
wget http://downloads.typesafe.com/typesafe-activator/1.2.10/typesafe-
activator-1.2.10.zip && \  
unzip typesafe-activator-1.2.10.zip && \  
rm -f /opt/typesafe-activator-1.2.10.zip && \  
mv /opt/activator-1.2.10 /opt/activator  
  
EXPOSE 8888  
EXPOSE 9000  
CMD ["/opt/activator/activator", "ui", "-Dhttp.address=0.0.0.0",
"-Dorg.slf4j.simpleLogger.defaultLogLevel=trace"]  

