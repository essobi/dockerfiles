FROM node:7.10-alpine  
ADD . /src  
WORKDIR /src  
RUN apk add --update python build-base && cd /src && yarn install  
CMD ["node", "app.js", "--cron", "0 10 0 * * 6", "--run"]  

