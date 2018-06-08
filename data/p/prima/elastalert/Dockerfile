FROM ivankrizsan/elastalert:0.1.8  
ENV ELASTICSEARCH_HOST search-kibana-1.prima.prod  
  
RUN pip install awscli  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/opt/start-elastalert.sh"]  

