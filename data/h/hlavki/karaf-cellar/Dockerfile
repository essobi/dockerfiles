FROM hlavki/karaf:4.0  
MAINTAINER Michal Hlavac <miso@hlavki.eu>  
  
ENV CELLAR_VERSION 4.0.3  
  
RUN sed -i '/featuresRepositories\s*=\s*/a \ \ \ \
mvn:org.apache.karaf.cellar\/apache-karaf-
cellar\/'$CELLAR_VERSION'\/xml\/features,\ \\'
/opt/karaf/etc/org.apache.karaf.features.cfg; \  
sed -i '/featuresBoot\s*=\s*/a \ \ \ \ cellar,\ \\'
/opt/karaf/etc/org.apache.karaf.features.cfg  
  
EXPOSE 54327/udp 4242  

