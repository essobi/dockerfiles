FROM java:8  
MAINTAINER Vinayak Bhadage <vinayak.bhadage@gmail.com>  
  
ENV LAST_EXECUTION_START "2014-06-06T09:08:00.948Z"  
ENV INDEX_NAME **NONE**  
ENV CLUSTER **NONE**  
ENV ES_HOST **NONE**  
ENV ES_PORT "9300"  
ENV SCHEDULE "0 0/10 * * * ?"  
ENV SQL_SERVER_HOST **NONE**  
ENV DB_NAME **NONE**  
ENV DB_USER_NAME **NONE**  
ENV DB_PASSWORD **NONE**  
  
ADD bin /data-importer/bin  
ADD lib /data-importer/lib  
  
RUN chmod +x /data-importer/bin/*.sh  
  
VOLUME ["/data-importer"]  
  
WORKDIR /data-importer  
  
CMD ["/data-importer/bin/run.sh"]  

