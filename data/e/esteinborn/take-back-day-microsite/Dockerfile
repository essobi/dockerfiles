FROM node:9  
# Run all commands from this location  
WORKDIR /usr/src/app  
  
# Copy in the App code  
COPY . .  
  
# Install dependencies  
RUN yarn  
  
# Build an optimized production build  
RUN yarn build  
  
# We're serving from port 5000  
EXPOSE 5000  
# Run the server  
CMD ["node", "server"]

