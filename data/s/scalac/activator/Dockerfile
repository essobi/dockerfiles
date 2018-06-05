FROM scalac/java8:latest  
  
MAINTAINER Jakub Zubielik <jakub.zubielik@scalac.io>  
  
ENV PATH $PATH:/opt/activator  
ENV VERSION 1.3.7  
RUN cd /opt && \  
wget https://downloads.typesafe.com/typesafe-activator/$VERSION/typesafe-
activator-$VERSION.zip && \  
unzip typesafe-activator-$VERSION.zip && \  
rm -f /opt/typesafe-activator-$VERSION.zip && \  
mv /opt/activator-dist-$VERSION /opt/activator  
  
EXPOSE 8888 9000  
CMD ["/opt/activator/activator", "ui", "-Dhttp.address=0.0.0.0",
"-Dorg.slf4j.simpleLogger.defaultLogLevel=trace"]  

