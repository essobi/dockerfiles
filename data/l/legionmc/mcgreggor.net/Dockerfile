# Use node 9.4.0 LTS  
FROM node:9.4.0  
# Copy source code  
COPY . /app  
  
# Change working directory  
WORKDIR /app  
  
# Install dependencies  
RUN npm install  
  
# Expose API port to the outside  
EXPOSE 8080  
# Launch application  
CMD ["npm","start"]  

