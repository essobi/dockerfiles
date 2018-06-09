FROM elasticsearch:2.4.0  
MAINTAINER thangtd90@gmail.com  
  
COPY elasticsearch-analysis-vietnamese-2.4.0.zip /usr/share/elasticsearch/  
  
RUN cd /usr/share/elasticsearch && \  
bin/plugin install file:elasticsearch-analysis-vietnamese-2.4.0.zip && \  
bin/plugin install analysis-kuromoji && \  
bin/plugin install analysis-icu  
  

