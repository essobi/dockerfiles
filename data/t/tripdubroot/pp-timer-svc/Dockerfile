FROM node:alpine  
  
COPY . /app  
WORKDIR /app  
RUN npm install  
  
EXPOSE 3001  
ENTRYPOINT ["npm", "start"]  
  
# docker run -d --name timer -p 3001:3001 --net=pixel timer

