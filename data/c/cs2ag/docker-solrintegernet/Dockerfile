# Base image  
FROM openjdk:8-jre-alpine  
  
MAINTAINER Stefan Preissner <github@cs2.ch>  
  
# Install required packages  
RUN apk add --no-cache --update \  
wget procps bash rsync  
  
# Add user for Solr  
RUN set -x \  
&& addgroup -g 1000 -S solr \  
&& adduser -u 1000 -D -S -G solr solr  
  
# Download solr  
RUN mkdir -p /usr/local/solr && \  
cd /usr/local/solr/ && \  
wget --no-check-certificate
https://archive.apache.org/dist/lucene/solr/6.6.0/solr-6.6.0.tgz && \  
tar -xvzf solr-6.6.0.tgz && \  
rm solr-6.6.0.tgz  
  
# Create data directory  
RUN mkdir /usr/local/solr/solr-6.6.0/server/solr/data  
  
# Add special configuration  
ADD conf/ /usr/local/solr/solr-6.6.0/server/solr/  
  
# Change owner of solr directory  
RUN chown -R solr:solr /usr/local/solr/solr-6.6.0  
  
# Sync directory before mount is created  
RUN rsync -a /usr/local/solr/solr-6.6.0/server/solr /var/tmp/  
  
# Add startup script  
ADD startup /usr/bin/startup  
  
# Make startup script executable  
RUN chmod 755 /usr/bin/startup  
  
# Expose port 8983  
EXPOSE 8983  
# Run solr  
CMD [ "/usr/bin/startup" ]  

