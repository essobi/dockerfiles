FROM elasticsearch:1.7.2  
MAINTAINER Brandfolder, Inc. <developers@brandfolder.com>  
  
# RUN /usr/share/elasticsearch/bin/plugin install delete-by-query --verbose  
# Install confd  
RUN wget
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 -O ./bin/confd  
RUN chmod +x ./bin/confd  
ADD confd /etc/confd  
  
# Add Entrypoint  
COPY ./bin ./bin  
RUN chmod +x ./bin  
RUN chmod +x ./bin/config.sh  
RUN chmod +x ./bin/entrypoint.sh  
ENTRYPOINT [ "./bin/entrypoint.sh" ]  
  
# Default ENV  
ENV ES_NETWORK_HOST 0.0.0.0  
ENV PORT 9200  
# Default Command  
CMD [ "elasticsearch" ]  

