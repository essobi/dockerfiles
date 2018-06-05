FROM node:alpine  
  
RUN apk add tzdata --update --no-cache && cp /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime && echo "Asia/Shanghai" /etc/localtime && apk del tzdata  
  
RUN npm i -g --production brickyard-cli@^5.1.0 && npm cache clean --force  
  
CMD ["brickyard"]  

