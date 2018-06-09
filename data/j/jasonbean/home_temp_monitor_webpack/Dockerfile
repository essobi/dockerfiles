FROM node:8-alpine  
  
RUN mkdir -p /home/webapp  
COPY . /home/webapp  
WORKDIR /home/webapp  
  
RUN npm install  
RUN npm run build  
RUN npm prune --production  
  
VOLUME [/config]  
EXPOSE 8080  
USER nobody  
CMD [ "npm", "start" ]

