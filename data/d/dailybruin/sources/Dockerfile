# Use LTS version of node  
FROM
node:carbon@sha256:ceb6e9e47ec034664e795d7b7e45f288e2b47a5a51cc6015dc7d672252900788  
  
ENV NODE_ENV production  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json yarn.lock ./  
  
RUN yarn --production=false  
# If you are building your code for production  
# RUN npm install --only=production  
# Bundle app source  
COPY . .  
  
EXPOSE 3000  
CMD yarn start  

