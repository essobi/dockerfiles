# Use node 8.2.1  
FROM node:8.2.1  
ENV DEBIAN_FRONTEND noninteractive  
  
# Copy source code  
COPY . /app  
  
# Change working directory  
WORKDIR /app  
  
# Install dependencies  
RUN apt-get update  
RUN chown node:node -R .  
RUN npm install  
  
# Launch application  
CMD ["yarn","start"]

