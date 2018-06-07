From php:7.2-fpm  
  
RUN groupadd -g 999 phpuser && \  
useradd -r -u 999 -g phpuser phpuser  
USER phpuser  
  
WORKDIR /app  
VOLUME /app  
  
EXPOSE 9000  
ENTRYPOINT ["docker-php-entrypoint"]  
CMD ["php-fpm"]  

