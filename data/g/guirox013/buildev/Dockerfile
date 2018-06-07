FROM node:7.8.0  
# Copy list of server side dependencies  
COPY package.json /tmp/package.json  
  
# Install dependencies  
RUN cd /tmp && npm install --loglevel=warn  
  
# Copy dependencies libraries  
RUN mkdir /app && cp -a /tmp/node_modules /app/  
  
# Copy src files  
COPY . /app/  
  
# Use /app working directory  
WORKDIR /app  
  
EXPOSE 3100  
CMD ["npm", "run", "dev"]

