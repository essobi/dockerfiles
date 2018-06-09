FROM node:9.2.0  
# Create app directory  
WORKDIR /app  
  
# Copy package.json and package-lock.json  
COPY package*.json ./  
  
# Install deps  
RUN npm install --only=production  
  
COPY . ./  
  
ENV HOST 0.0.0.0  
ENV PORT 10010  
EXPOSE $PORT  
CMD ["npm", "start"]  

