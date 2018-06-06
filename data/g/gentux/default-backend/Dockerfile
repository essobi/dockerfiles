FROM node:4.5  
ENV NODE_ENV=production  
ENV NODE_PORT=80  
EXPOSE 80  
ADD . /var/www  
RUN cd /var/www && npm install  
  
WORKDIR /var/www  
CMD ["node", "src/index.js"]  

