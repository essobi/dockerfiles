FROM node:0.12-slim  
  
  
# Create app directory  
RUN mkdir -p /usr/concierge  
WORKDIR /usr/concierge  
  
COPY package.json .  
RUN npm install  
  
COPY . /usr/concierge  
RUN [ -f package.json.bak ] && mv package.json.bak package.json || echo ""  
  
CMD ["./node_modules/pm2/bin/pm2", "start", "main.js", "--no-daemon"]  

