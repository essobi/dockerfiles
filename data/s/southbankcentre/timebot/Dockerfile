FROM alpine  
  
RUN apk add --update nodejs  
  
COPY package.json /src/package.json  
RUN cd /src; npm install --production  
  
COPY . /src  
  
CMD ["node", "/src/bin/bot.js"]

