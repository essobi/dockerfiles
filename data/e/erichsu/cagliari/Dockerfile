FROM mhart/alpine-node:6  
MAINTAINER TingYao Hsu tingyaohsu@tutorabc.com  
  
# Install dependancies  
ADD . /app  
WORKDIR /app  
RUN apk add --no-cache git cairo-dev make g++ gcc bash curl  
RUN npm i --unsafe-perm && npm run build  
  
# Clean packages and cache  
RUN npm ddp && npm cache clean && npm prune --production  
RUN apk del --purge git cairo-dev make g++ gcc bash  
  
# Start service  
CMD npm start

