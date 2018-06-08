FROM elasticsearch:2.3.4  
EXPOSE 9200:9200  
EXPOSE 9300:9300  
# Install plugins  
RUN cd /usr/share/elasticsearch && \  
bin/plugin install license && \  
bin/plugin install marvel-agent && \  
bin/plugin install analysis-icu  
  
MAINTAINER Alexandr Kulitsky <kulitsky@targetprocess.com>

