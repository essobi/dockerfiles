FROM postgres:9.5  
ENV TZ=Europe/Moscow  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN chmod 0666 /etc/localtime && chmod 0666 /etc/timezone  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]

