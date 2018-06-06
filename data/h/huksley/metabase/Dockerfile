FROM java:openjdk-7-jre-alpine  
  
ENV JAVA_HOME=/usr/lib/jvm/default-jvm  
ENV PATH /usr/local/bin:$PATH  
ENV FC_LANG en-US  
ENV LC_CTYPE en_US.UTF-8  
RUN apk add --update wget bash java-cacerts ttf-dejavu fontconfig && \  
ln -sf "${JAVA_HOME}/bin/"* "/usr/bin/" && \  
rm -f /usr/lib/jvm/default-jvm/jre/lib/security/cacerts && \  
ln -s /etc/ssl/certs/java/cacerts /usr/lib/jvm/default-
jvm/jre/lib/security/cacerts && \  
mkdir -p /app/source/target/uberjar && \  
mkdir -p /app/source/bin  
  
COPY start /app/source/bin  
COPY metabase.jar /app/source/target/uberjar  
RUN chmod a+x /app/source/bin/start  
  
EXPOSE 3000  
WORKDIR /app/source  
ENTRYPOINT ["./bin/start"]  

