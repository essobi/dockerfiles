# This is a docker Drupal environment for PNX QA and Staging.  
#  
FROM previousnext/base:latest  
MAINTAINER Nick Schuch <nick@previousnext.com.au>  
  
ENV SOLR_VERSION 4.7.0  
##  
# Packages.  
##  
RUN apt-get update -y  
RUN apt-get install -y openjdk-7-jre-headless tar  
  
##  
# Configure Solr 4.x.  
##  
RUN mkdir -p /opt  
ADD
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz
/opt/solr-$SOLR_VERSION.tgz  
RUN tar -C /opt --extract --file /opt/solr-$SOLR_VERSION.tgz  
RUN mv /opt/solr-$SOLR_VERSION /opt/solr  
  
##  
# Add search_api configuration.  
##  
ADD ./conf/solr /opt/search_api  
RUN rsync -avz /opt/search_api/* /opt/solr/example/solr/collection1/conf/  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /root/start.sh  
RUN chmod 755 /root/start.sh  
  
##  
# Setup supervisord.  
##  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
  
EXPOSE 8983  
CMD ["/root/start.sh"]  

