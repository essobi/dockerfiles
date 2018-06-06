FROM mhart/alpine-node:4.4  
# Build  
RUN mkdir -p /app  
ADD package.json /app  
WORKDIR /app  
RUN npm install --production  
  
# Copy files  
ADD . /app  
  
EXPOSE 5000  
# Start  
CMD ["npm", "start"]  

