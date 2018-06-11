FROM node:4  
RUN mkdir -p /hubot-tryout && mkdir -p /usr/src/app  
WORKDIR /hubot-tryout  
  
RUN npm init -y && npm install -g coffee-script && npm install hubot  
  
EXPOSE 8080  
CMD "node_modules/hubot/bin/hubot"  
  
ONBUILD COPY . /usr/src/app/  
ONBUILD RUN npm install /usr/src/app  
  

