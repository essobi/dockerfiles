FROM alpine:3.5  
MAINTAINER Clutch  
  
WORKDIR /bot  
  
RUN apk update && apk upgrade && apk --no-cache add --virtual wget ca-
certificates  
RUN apk add --update nodejs  
  
RUN npm install gulp-cli -g  
  
RUN wget --no-check-certificate -O master.zip
https://github.com/lbjdaking23/ClutchBot/archive/master.zip  
RUN unzip master.zip  
RUN mv ClutchBot-master/* .  
RUN rm -rf ClutchBot-master  
  
RUN ls  
  
RUN npm i  
RUN gulp prod  
  
CMD node dist/ -u $BOT_USERNAME -t $BOT_TOKEN -c $BOT_CHANNEL  

