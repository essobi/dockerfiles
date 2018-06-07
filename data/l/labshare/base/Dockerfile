FROM keymetrics/pm2:8-alpine  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash git openssh  
  
# Add global node packages  
RUN npm i -g lsc  

