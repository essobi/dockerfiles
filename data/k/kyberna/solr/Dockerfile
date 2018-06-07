FROM java:jre  
MAINTAINER Seti <sebastian.koehlmeier@kyberna.com>  
  
ENV SOLR_USER solr  
ENV SOLR_UID 1000  
ENV SOLR_VERSION 6.6.2  
ENV SOLR solr-$SOLR_VERSION  
  
RUN \  
groupadd -g $SOLR_UID $SOLR_USER && \  
useradd -u $SOLR_UID -g $SOLR_USER $SOLR_USER && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install wget openssh-client lsof curl procps && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt && \  
wget -nv --no-check-certificate --output-document=/opt/$SOLR.tgz
https://dist.apache.org/repos/dist/release/lucene/solr/$SOLR_VERSION/$SOLR.tgz
&& \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
ln -s /opt/$SOLR /opt/solr && \  
chown -R $SOLR_USER:$SOLR_USER /opt/solr && \  
chown -R $SOLR_USER:$SOLR_USER /opt/$SOLR  
  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
USER $SOLR_USER  
EXPOSE 8983  
CMD ["/bin/bash", "-c", "/run.sh"]  

