# Docker image for the command line use of SchemaCrawler.  
# http://sualeh.github.io/SchemaCrawler/  
FROM java:8  
MAINTAINER Adam <adam.bell-hanssen@symfoni.com>  
  
ENV SCHEMACRAWLER_VERSION 14.03.01  
RUN apt-get update && \  
apt-get install -y graphviz && \  
apt-get clean  
  
RUN wget
https://github.com/sualeh/SchemaCrawler/releases/download/v"$SCHEMACRAWLER_VERSION"/schemacrawler-"$SCHEMACRAWLER_VERSION"-main.zip
&& \  
unzip schemacrawler-"$SCHEMACRAWLER_VERSION"-main.zip && \  
rm schemacrawler-"$SCHEMACRAWLER_VERSION"-main.zip && \  
mv schemacrawler-"$SCHEMACRAWLER_VERSION"-main schemacrawler  
  
WORKDIR /schemacrawler/_schemacrawler  
  
VOLUME /output  
  
ENTRYPOINT ["./schemacrawler.sh"]  

