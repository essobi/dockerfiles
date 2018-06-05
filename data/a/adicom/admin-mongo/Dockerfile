FROM node:slim  
MAINTAINER Ivan Samoylenko (mutsmu@gmail.com)  
  
COPY . /app  
WORKDIR /app  
RUN cd /app && npm install --production && npm dedupe && npm prune
--production  
EXPOSE 1234  
CMD ["node", "app.js" ]  

