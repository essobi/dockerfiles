FROM mhart/alpine-node:5.11.1  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app  
RUN apk add --update git  
RUN npm install  
  
COPY lib /usr/src/app/lib  
COPY bin /usr/src/app/bin  
  
ENTRYPOINT ["node", "bin/overwriteJiraResultsInGoogleSheet.js"]  

