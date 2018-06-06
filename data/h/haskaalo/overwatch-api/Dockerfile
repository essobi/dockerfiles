FROM node:8-alpine  
  
WORKDIR /usr/src/app  
ADD . /usr/src/app/  
  
ENV NODE_ENV=production  
RUN yarn  
  
EXPOSE 3000  
CMD ["node", "server.js"]

