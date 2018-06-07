FROM python:3.6.3-alpine3.6  
  
ENV INTERVAL_IN_HOURS=24  
ENV OLDER_THAN_IN_DAYS=20  
ENV ES_HOST=elasticsearch  
ENV ES_PORT=9200  
  
RUN adduser -D curator curator \  
&& pip install elasticsearch-curator==5.2.0  
  
ADD docker-entrypoint.sh /  
ADD action_file.yml /  
ADD config.yml /  
  
USER curator:curator  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["curator"]  

