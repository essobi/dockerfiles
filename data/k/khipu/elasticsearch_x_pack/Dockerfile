FROM elasticsearch:5.1.1  
MAINTAINER developers@khipu.com  
RUN usermod --uid 2000 elasticsearch && groupmod --gid 2000 elasticsearch && \  
bin/elasticsearch-plugin install x-pack --batch  

