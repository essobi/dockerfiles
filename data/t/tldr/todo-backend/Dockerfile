FROM node:5.1.0-slim  
  
RUN mkdir /app  
COPY node_modules /app/node_modules/  
COPY *.js package.json /app/  
COPY docker/start.sh /  
  
# We need this for polling mongo availability upon starting  
RUN apt-get update && \  
apt-get install -y netcat  
  
EXPOSE 8080  
CMD ["/start.sh"]

