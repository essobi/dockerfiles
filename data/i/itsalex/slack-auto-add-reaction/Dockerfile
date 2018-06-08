FROM node:10-alpine  
  
ADD src /slack-auto-add-reaction/src/  
COPY package.json /slack-auto-add-reaction/package.json  
  
WORKDIR /slack-auto-add-reaction  
  
RUN npm install && npm run build  
  
CMD [ "/usr/local/bin/node", "/slack-auto-add-reaction/build/index.js" ]

