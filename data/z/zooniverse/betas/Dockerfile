FROM zooniverse/nodejs  
  
ADD package.json /app/package.json  
WORKDIR /app  
  
RUN npm install  
  
ADD ./ /app/  
  
ENTRYPOINT [ "npm", "run-script" ]  

