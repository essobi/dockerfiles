FROM node:8-alpine  
  
RUN npm install pm2 -g  
  
VOLUME ["/app"]  
  
# Expose ports  
EXPOSE 3000  
WORKDIR /app  
  
COPY ./docker-entrypoint.sh /  
RUN chmod a+x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["production"]  

