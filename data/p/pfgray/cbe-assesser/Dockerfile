FROM node:argon  
  
COPY ./ /app  
WORKDIR /app  
RUN npm install  
RUN npm run build  
  
EXPOSE 9000  
CMD ["/bin/bash", "/app/docker/run.sh"]  

