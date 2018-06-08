FROM tutum/curl:trusty  
  
MAINTAINER "Martin Westergaard Lassen <martin@mwl.dk>"  
ENV ELASTIC_SEARCH_URL="http://elasticsearch:9200"  
COPY import.sh /  
COPY index.json /  
  
RUN curl -s
https://www.elastic.co/guide/en/kibana/3.0/snippets/shakespeare.json >
shakespeare.json  
  
CMD /import.sh  

