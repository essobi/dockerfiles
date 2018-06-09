FROM ubuntu:14.04  
MAINTAINER Nikitas Tampakis <nikitas.tampakis@gmail.com>  
  
ENV SOLR_VERSION 5.1.0  
ENV JETTY 4.10.4  
ENV SOLR solr-$SOLR_VERSION  
ENV SOLR_USER solr  
ENV SOLR_BL blacklight-jetty-$JETTY  
ENV APP_NAME orangelight  
ENV SOLR_HOME /opt/cores  
  
RUN apt-get update && apt-get -y install \  
unzip \  
wget \  
git \  
curl \  
openjdk-7-jdk \  
nano  
  
WORKDIR /opt  
  
RUN \  
wget http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz && \  
mkdir solr && \  
tar -xzf $SOLR.tgz -C solr --strip-components=1 && \  
wget https://github.com/projectblacklight/blacklight-jetty/archive/v$JETTY.zip  
  
RUN \  
unzip v$JETTY.zip && \  
mkdir cores && \  
mv $SOLR_BL/solr/* cores/ && \  
rm v$JETTY.zip && \  
rm -r $SOLR_BL  
  
RUN git clone https://github.com/pulibrary/orangelight.git  
RUN cp -r orangelight/solr_conf/conf/* cores/blacklight-core/conf  
RUN sed -i s/'side="front"'/''/g cores/blacklight-core/conf/schema.xml  
  
EXPOSE 8983  
WORKDIR /opt/solr  
  
#CMD ["/bin/bash", "-c", "bin/solr -f"]

