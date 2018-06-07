FROM elasticsearch:1.6  
MAINTAINER developers@khipu.com  
  
RUN usermod --uid 2000 elasticsearch && groupmod --gid 2000 elasticsearch && \  
cd /usr/share/elasticsearch/bin && \  
./plugin install royrusso/elasticsearch-HQ/v1.0.0  

