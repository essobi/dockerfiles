FROM alpine:3.5  
RUN apk add --no-cache docker nodejs bash findutils libewf  
  
ADD ./package.json /usr/local/src/  
WORKDIR /usr/local/src/  
  
RUN npm install --only=production  
  
ADD ./ /usr/local/src/  
  
CMD ["npm", "start"]  

