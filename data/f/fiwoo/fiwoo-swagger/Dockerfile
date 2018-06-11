FROM swaggerapi/swagger-ui:latest  
  
MAINTAINER fiwoo  
  
# Install nodejs  
RUN apk add \--update nodejs  
  
COPY . .  
  
# Install swagger-combine  
RUN npm set progress=false && npm config set depth 0 && npm cache clean
--force  
RUN npm i \--loglevel=error  
  
# Execute combine script  
RUN chmod +x combine.sh  
RUN sh combine.sh  
  
ENV API_URL ""  
ENV SWAGGER_JSON "/swagger.json"  
# Configure cron to execute combine script periodically  
RUN crontab -l | { cat; echo "*/10 * * * * cd / && sh combine.sh >>
/var/log/cron.log 2>&1"; } | crontab -  
  
CMD ["sh", "docker-run.sh"]  

