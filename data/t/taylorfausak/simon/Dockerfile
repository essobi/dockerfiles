FROM mhart/alpine-node:6.6.0  
WORKDIR /hubot  
COPY package.json /hubot/package.json  
RUN npm install  
COPY external-scripts.json /hubot/external-scripts.json  
CMD npm run hubot  

