FROM google/nodejs  
  
WORKDIR /app  
ADD package.json /app/  
RUN npm install  
ADD . /app  
  
EXPOSE 9966  
CMD []  
ENTRYPOINT ["/nodejs/bin/npm", "start"]  

