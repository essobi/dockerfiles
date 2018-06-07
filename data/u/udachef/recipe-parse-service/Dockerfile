# Get the node image  
FROM node:boron  
  
COPY package.json package.json  
RUN yarn  
  
# Add your source files  
COPY . .  
  
# Start the service  
CMD ["npm","start"]

