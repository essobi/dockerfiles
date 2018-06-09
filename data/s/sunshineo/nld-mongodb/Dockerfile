FROM sunshineo/docker-mongodb:latest  
  
COPY ./local.sh /local.sh  
COPY ./www.sh /www.sh  
COPY ./nld-mongo-entrypoint.sh /nld-mongo-entrypoint.sh  
  
ARG BUILD_ENV  
COPY ./pick-config.sh /pick-config.sh  
RUN ./pick-config.sh  
  
ENTRYPOINT ["/nld-mongo-entrypoint.sh"]  
CMD ["mongod"]

