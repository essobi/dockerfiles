FROM node:4  
MAINTAINER Jarle Fosen <jarlefosen@gmail.com>  
  
RUN npm install --silent -g nodemon  
  
RUN mkdir /app  
WORKDIR /app  
COPY package.json ./  
RUN npm install  
  
COPY mining* ./  
  
ENV REDIS_DB_HOST localhost  
ENV TWITTER_TAGS dagenatifi  
ENV INSTAGRAM_TAGS "#dagenatifi"  
ENV TWITTER_CONSUMER_KEY ""  
ENV TWITTER_CONSUMER_SECRET ""  
ENV TWITTER_TOKEN_KEY ""  
ENV TWITTER_TOKEN_SECRET ""  
ENV INSTAGRAM_TOKEN_KEY ""  
CMD node mining.js  

