FROM apsl/thumbor:6.3.0  
MAINTAINER Fernando Barbosa <fernando.barbosa@quintoandar.com.br>  
  
# Install New Relic  
ENV NR_APP_NAME thumbor  
RUN pip install newrelic && \  
newrelic-admin generate-config invalid-key > newrelic.ini && \  
sed -i "/^\\[newrelic\\]/c\\[newrelic]\nfeature_flag =
tornado.instrumentation.r3" newrelic.ini  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["thumbor"]  
  
EXPOSE 8000  

