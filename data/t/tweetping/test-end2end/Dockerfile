FROM node:6  
WORKDIR /src  
  
COPY package.json /src/package.json  
  
RUN npm install  
  
COPY end_to_end.js /src/end_to_end.js  
COPY tweet.json /src/tweet.json  
COPY fb_feed.json /src/fb_feed.json  
  
CMD npm test  

