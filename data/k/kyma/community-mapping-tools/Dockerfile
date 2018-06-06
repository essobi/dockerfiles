FROM google/nodejs  
  
WORKDIR /app  
  
# Install npm modules.  
ADD package.json /app/  
RUN npm install  
  
ADD . /app  
  
# Build frontend code  
RUN npm run build-prod  
  
ENV DOCKER true  
ENV NODE_ENV production  
EXPOSE 8080  
CMD ["./node_modules/.bin/coffee", "index.coffee"]  

