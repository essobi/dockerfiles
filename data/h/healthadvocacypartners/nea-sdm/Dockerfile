# Use node ^v9  
FROM node:9  
# Labels  
LABEL maintainer="admin@healthadvocacypartners.com"  
  
# Establish Working Directory for App in Container  
WORKDIR /app  
  
# Copy package.json file into /app directory on container  
COPY package.json /app  
  
# Install node dependencies  
RUN npm install  
  
# Copy application code to /app directory on container  
COPY . /app  
  
# Set environment variables  
ENV PORT 8080  
# Run build script  
RUN npm run build  
  
# Expose port 8080 on container to outside world. Hi mom!  
EXPOSE 8080  
# Run the app  
CMD npm run serve  
  

