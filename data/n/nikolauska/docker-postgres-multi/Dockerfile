# vim:set ft=dockerfile:  
FROM postgres:alpine  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["postgres"]  

