FROM anapsix/alpine-java:8_server-jre  
  
ENV H2_URL http://storage.googleapis.com/google-code-archive-
downloads/v2/code.google.com/h2database/h2-2013-07-28.zip  
ENV VERSION 0.1  
ENV APPROOT /tmp/h2/bin  
  
WORKDIR $APPROOT  
  
# Web Console port  
EXPOSE 8082  
# TCP port  
EXPOSE 9092  
# PG server port  
EXPOSE 5435  
RUN wget $H2_URL -O /tmp/h2.zip && \  
cd /tmp && \  
unzip -qq h2.zip  
  
CMD ["java", "-jar", "/tmp/h2/bin/h2-1.3.173.jar", "-webAllowOthers",
"-tcpAllowOthers"]  
  

