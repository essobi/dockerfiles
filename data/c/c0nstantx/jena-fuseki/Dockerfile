#  
# Apache Jena + TDB + Fuseki  
#  
# RDF API with triple store persistent layer along with REST API  
#  
# Pull base image.  
FROM alpine  
  
MAINTAINER Konstantinos Christofilos <kostasxx@gmail.com>  
  
# Update distro  
RUN apk update  
  
# Install some tools  
RUN apk add bash curl  
  
# Install JAVA  
RUN apk add openjdk8-jre  
  
# Install Fuseki 2  
RUN curl -SL "http://apache.cc.uoc.gr/jena/binaries/apache-jena-
fuseki-2.3.1.tar.gz" -o fuseki.tar.gz  
  
RUN tar zxvf fuseki.tar.gz && \  
mv apache-jena-fuseki-2.3.1 /apache-fuseki && \  
rm fuseki.tar.gz  
  
ADD ./shiro.ini /apache-fuseki/run/shiro.ini  
  
ENV FUSEKI_PORT 3030  
ENV FUSEKI_DATASET ds  
  
ADD ./run.sh /run.sh  
RUN chmod +x /run.sh  
  
RUN mkdir /db  
  
WORKDIR /apache-fuseki  
  
CMD ["/run.sh"]

