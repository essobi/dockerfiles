FROM node:carbon-alpine  
  
MAINTAINER cronic@zensystem.io  
  
RUN apk add --no-cache git  
  
USER node  
  
ENV NODE_ENV=production  
  
RUN cd ~ \  
&& git clone -b insight-zencashjs https://github.com/ZencashOfficial/zen-
tipbot.git \  
&& cd ./zen-tipbot \  
&& npm install \  
&& npm run build  
  
WORKDIR /home/node/zen-tipbot  
  
CMD ["npm","run","prod"]  
  

