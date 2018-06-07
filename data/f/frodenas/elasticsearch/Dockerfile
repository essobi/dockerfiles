FROM frodenas/java7  
MAINTAINER Ferran Rodenas <frodenas@gmail.com>  
  
# Install Elasticsearch 1.3.1  
RUN cd /tmp && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.1.tar.gz
&& \  
tar xvzf elasticsearch-1.3.1.tar.gz && \  
mv /tmp/elasticsearch-1.3.1 /elasticsearch && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add scripts  
ADD scripts /scripts  
RUN chmod +x /scripts/*.sh  
  
# Command to run  
ENTRYPOINT ["/scripts/run.sh"]  
CMD [""]  
  
# Expose listen port  
EXPOSE 9200  
EXPOSE 9300  
# Expose our data and logs volumes  
VOLUME ["/data", "/logs"]  

