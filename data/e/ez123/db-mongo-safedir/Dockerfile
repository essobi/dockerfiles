# v1.0.0 2017-10-26 webmaster@highskillz.com  
#  
FROM ez123/db-mongo:3.2b  
  
ENV SFD_ENTRYPOINT="/usr/local/bin/docker-entrypoint.keygen.sh"  
COPY src/entrypoint-safedir.sh ./docker-entrypoint.safedir.sh  
RUN chmod a+x ./docker-entrypoint.safedir.sh  
  
ENTRYPOINT [ "./docker-entrypoint.safedir.sh" ]  
CMD ["mongod"]  
  

