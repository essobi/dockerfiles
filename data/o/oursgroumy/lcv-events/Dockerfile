FROM node:slim  
WORKDIR /app  
COPY . /app  
ENV NODE_ENV=prod  
RUN cd /app && npm install  
CMD npm run-script start-prod  
EXPOSE 3001

