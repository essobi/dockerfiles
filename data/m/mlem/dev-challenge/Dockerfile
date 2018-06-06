# Using much more light-weight node container  
FROM mhart/alpine-node  
  
WORKDIR /tmp  
COPY package.json /tmp/  
RUN npm config set registry http://registry.npmjs.org/ && npm install  
  
# Install process manager globally  
RUN npm install pm2 -g  
  
WORKDIR /usr/src/app  
  
RUN cp -a /tmp/node_modules /usr/src/app  
  
COPY . ./  
  
RUN npm run build -- --release  
  
EXPOSE 3000  
# Start the app with pm2  
CMD ["pm2", "start", "processes.json", "--no-daemon"]  

