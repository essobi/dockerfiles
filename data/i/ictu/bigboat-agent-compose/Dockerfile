FROM docker:1.10.3  
RUN apk --update --no-cache add nodejs coreutils 'py-pip==8.1.2-r0' && pip
install 'docker-compose==1.9.0'  
  
ADD . /app  
  
WORKDIR /app  
  
RUN npm install  
  
EXPOSE 80  
CMD ["npm", "start"]  

