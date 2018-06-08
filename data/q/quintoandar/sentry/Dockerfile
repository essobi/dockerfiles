FROM sentry:8.20  
ADD custom-entrypoint.sh /bin/  
  
ADD config.yml /etc/sentry/config.yml  
  
RUN pip install newrelic  
  
ENTRYPOINT ["custom-entrypoint.sh"]  

