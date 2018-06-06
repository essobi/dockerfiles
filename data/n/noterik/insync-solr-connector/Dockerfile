FROM python:2.7.14-alpine  
  
RUN apk add --no-cache curl  
  
RUN pip install --no-cache-dir 'mongo-connector[solr]'  
  
ADD ./wait-for-solr.sh /wait-for-solr.sh  
ADD ./start.sh /start.sh  
ADD ./config.json /config.json  
  
RUN chmod +x *.sh  
  
RUN touch mongo-connector.log  
  
CMD tail -f mongo-connector.log  

