# FROM mhart/alpine-node:8  
FROM yuxizhe/node  
WORKDIR /app  
COPY . .  
RUN npm install  
RUN npm run build  
EXPOSE 8080  
CMD npm run start

