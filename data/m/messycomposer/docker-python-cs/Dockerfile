FROM python:3  
COPY sample-project/ /usr/src/sample-project  
COPY docker-entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
RUN usermod -u 1001 www-data \  
&& groupmod -g 1001 www-data  
  
VOLUME /usr/src/app  
  
ENTRYPOINT ["/entrypoint.sh"]  
WORKDIR /usr/src/app  
  
EXPOSE 8080  
CMD python -m project

