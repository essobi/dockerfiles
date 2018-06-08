FROM openjdk:8-jre  
  
MAINTAINER William Turner <william.turner@aero.bombardier.com>  
  
RUN apt-get update -y && apt-get install -y python && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PRESTO_VERSION 0.186  
RUN mkdir -p /opt/presto && \  
curl -LS https://repo1.maven.org/maven2/com/facebook/presto/presto-
server/${PRESTO_VERSION}/presto-server-${PRESTO_VERSION}.tar.gz | tar -xz
--strip-components=1 -C /opt/presto && \  
curl -Lo /usr/local/bin/presto
https://repo1.maven.org/maven2/com/facebook/presto/presto-
cli/${PRESTO_VERSION}/presto-cli-${PRESTO_VERSION}-executable.jar && \  
chmod +x /usr/local/bin/presto  
  
COPY ["./etc", "/opt/presto/etc"]  
  
EXPOSE 8080  
CMD ["/opt/presto/bin/launcher", "run"]  

