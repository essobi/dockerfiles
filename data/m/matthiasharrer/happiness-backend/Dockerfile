FROM node:7.5.0  
WORKDIR /var/www  
  
ADD src /var/www  
  
RUN npm install  
  
CMD ["node", "--harmony-async-await", "bin/www"]

