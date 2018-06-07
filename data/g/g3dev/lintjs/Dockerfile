FROM node:alpine  
  
WORKDIR /home/node  
  
COPY package.json .  
COPY runlint.sh .  
  
RUN npm install  
  
CMD ["./runlint.sh"]  

