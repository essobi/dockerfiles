FROM cogniteev/oracle-java:java8  
MAINTAINER Cogniteev <tech@cogniteev.com>  
  
ENV TIKA_VERSION=1.8.1  
  
ADD http://storage.googleapis.com/third-parties/tika-
server-${TIKA_VERSION}.jar /var/lib/tika/  
  
EXPOSE 10000  
CMD java -jar /var/lib/tika/tika-server-${TIKA_VERSION}.jar \  
\--host 0.0.0.0 \  
\--port 10000  

