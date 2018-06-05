FROM openjdk:8-jre  
  
MAINTAINER fumi@fumi.me  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV BLAZEGRAPH_NAME blazegraph  
ENV BLAZEGRAPH_VERSION 2.1.4  
ENV BLAZEGRAPH_VERSION_URL
http://sourceforge.net/projects/bigdata/files/bigdata/${BLAZEGRAPH_VERSION}/${BLAZEGRAPH_NAME}.jar/download  
  
  
COPY RWStore.properties /  
COPY start.sh /  
RUN chmod 755 /start.sh  
  
RUN wget -O ${BLAZEGRAPH_NAME}.jar $BLAZEGRAPH_VERSION_URL  
  
RUN mkdir -p /data  
VOLUME /data  
WORKDIR /data  
EXPOSE 9999  
ENTRYPOINT ["/start.sh"]  
CMD ["4g"]  

