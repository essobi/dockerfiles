FROM alpine:latest  
RUN apk add --no-cache openjdk8-jre  
ENV JAVA_HOME=/usr  
ENV PATH=$PATH:$JAVA_HOME  
RUN apk add --no-cache wget && \  
cd /home && \  
wget "http://mirrors.m247.ro/apache/nifi/1.1.2/nifi-1.1.2-bin.tar.gz" && tar
-xzf nifi-1.1.2-bin.tar.gz -C /home/ && \  
rm /home/nifi-1.1.2-bin.tar.gz && \  
apk del wget  
EXPOSE 8080  
ENTRYPOINT ["sh","/home/nifi-1.1.2/bin/nifi.sh","run"]  
CMD ["/bin/sh"]

