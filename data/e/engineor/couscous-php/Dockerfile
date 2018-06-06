FROM composer:latest  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
RUN composer global require couscous/couscous && \  
ln -s /composer/vendor/bin/couscous /usr/local/bin  
  
CMD ["couscous"]  
  
EXPOSE 8000  

