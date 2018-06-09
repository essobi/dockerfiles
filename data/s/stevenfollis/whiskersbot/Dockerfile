# Uses slim as Alpine is unavailable for 7.* and 8.* breaks the Web App  
FROM node:7.10-slim  
  
# Open Port 443 for https traffic  
EXPOSE 443  
# Copy application files into container  
COPY . /app  
  
# Install dependencies via npm  
WORKDIR /app  
RUN npm install  
  
# Start application  
CMD ["npm", "start"]

