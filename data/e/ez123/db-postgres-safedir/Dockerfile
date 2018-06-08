# v1.0.0 2017-10-26 webmaster@highskillz.com  
#  
FROM ez123/db-postgres:9.5-ssl  
  
COPY src/entrypoint-safedir.sh ./docker-entrypoint-safedir.sh  
RUN chmod a+x ./docker-entrypoint-safedir.sh  
  
ENTRYPOINT [ "./docker-entrypoint-safedir.sh" ]  
CMD ["postgres"]

