FROM node:6.9.5-alpine  
  
# Copy application files  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
# Install Yarn and Node.js dependencies  
RUN npm install yarn --global --no-progress --silent --depth 0 && \  
yarn install --no-progress && \  
yarn run build -- --release  
  
CMD [ "node", "build/server.js" ]

