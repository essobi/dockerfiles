FROM anapsix/alpine-java:jre8  
MAINTAINER Conor Brennan <brennc27@tcd.ie>  
  
EXPOSE 3030  
RUN apk add --no-cache curl  
  
# Download tdbloader2 binary  
ENV JENA_ARCHIVE https://archive.apache.org/dist/  
ENV JENA_VERSION 3.2.0  
ENV JENA_DIR /opt/jena  
  
RUN mkdir $JENA_DIR && \  
curl $JENA_ARCHIVE/jena/binaries/apache-jena-$JENA_VERSION.tar.gz | tar zxf -
-C $JENA_DIR  
ENV PATH $JENA_DIR/apache-jena-$JENA_VERSION/bin:$PATH  
  
# Download fuseki-server binary  
ENV FUSEKI_VERSION 2.4.0  
ENV FUSEKI_DIR /opt/fuseki  
ENV FUSEKI_HOME $FUSEKI_DIR/apache-jena-fuseki-$FUSEKI_VERSION  
  
RUN mkdir $FUSEKI_DIR && \  
curl $JENA_ARCHIVE/jena/binaries/apache-jena-fuseki-$FUSEKI_VERSION.tar.gz |
tar zxf - -C $FUSEKI_DIR  
ENV PATH $FUSEKI_DIR/apache-jena-fuseki-$FUSEKI_VERSION:$PATH  
  
ENV OWL_DIR /opt/owl  
  
# This variable specifies which OWL ontology should be used in the system  
ENV OWL_FILE
https://raw.githubusercontent.com/labda/DINTO/68a29b568d6690fd04284feb06d152ca6e1e2e46/DINTO%201/DINTO_1.owl  
  
# Create indexed database from DINTO OWL  
WORKDIR $OWL_DIR  
RUN curl $OWL_FILE -o ddis.owl  
RUN SORT_ARGS="-m" tdbloader2 --loc $OWL_DIR/tdb ddis.owl && \  
rm -rf ddis.owl  
  
CMD ["fuseki-server", "--loc=/opt/owl/tdb", "/dinto"]  

