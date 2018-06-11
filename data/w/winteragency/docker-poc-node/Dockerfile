FROM node:6.12.3  
RUN npm install -g nodemon  
  
# Yarn caching so it doesn't rebuild everything  
COPY .yarn_cache /usr/local/share/.cache/yarn/v1/  
COPY package.json ./yarn.* /tmp/  
RUN cd /tmp && yarn install --no-bin-links && \  
mkdir -p /usr/src/app  
  
COPY . /usr/src/app/  
  
EXPOSE 3000  
WORKDIR /usr/src/app  
  
VOLUME ["/usr/src/app"]  
  
# Make node_modules available in workspace although it's not located there  
ENV NODE_PATH /tmp/node_modules  
  
# Wait for database port to be available before starting  
CMD ["npm", "start"]  

