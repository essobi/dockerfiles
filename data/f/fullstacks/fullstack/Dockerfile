FROM node:alpine  
RUN apk add --no-cache git && git clone
https://github.com/Deepankar01/HelloExpress.git && apk del --purge git && cd
HelloExpress && npm install  
EXPOSE 3000  
CMD npm start

