FROM node:latest  
  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app/  
  
# Install Node.js dependencies  
RUN yarn install --no-progress \  
&& yarn cache clean \  
&& chmod +x ./boot.sh  
  
CMD [ "sh", "./boot.sh" ]  

