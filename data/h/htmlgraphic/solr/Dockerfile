FROM dockerimages/docker-java-oracle:7  
MAINTAINER Jason Gegere  
  
ENV SOLR_VERSION 5.3.1  
ENV SOLR solr-$SOLR_VERSION  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get -y install lsof curl procps \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& wget -nv --output-document=/$SOLR.tgz
http://www.mirrorservice.org/sites/ftp.apache.org/lucene/solr/$SOLR_VERSION/$SOLR.tgz
\  
&& tar -C / --extract --file /$SOLR.tgz \  
&& rm /$SOLR.tgz \  
&& ln -s /$SOLR /solr  
EXPOSE 8983  
# We will Put Our Image dockerimages/systemd-solr over that you should
directly build that if you plan to run this in production  
CMD ["/bin/bash", "-c", "/$SOLR/bin/solr -f"]  

