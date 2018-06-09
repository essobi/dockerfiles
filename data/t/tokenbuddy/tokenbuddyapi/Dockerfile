FROM node:8.7-alpine  
  
WORKDIR /home/app  
  
# Install python and other dependencies via apk  
RUN apk update && apk add python g++ make && rm -rf /var/cache/apk/*  
ADD package.json /home/app  
RUN npm install  
ADD . /home/app  
RUN npm run build  
  
CMD ["npm", "start"]  
  
EXPOSE 8080  

