FROM node:alpine as builder  
LABEL maintainer Massimiliano Cannarozzo <maxcanna@gmail.com>  
  
ENV NODE_ENV=production  
ADD ./ /var/www/homeautomation/  
  
WORKDIR /var/www/homeautomation  
RUN apk update  
RUN apk add git python2 make g++ libpcap-dev yarn  
RUN mv constants.js.dist constants.js  
RUN yarn --ignore-engines  
  
FROM node:alpine  
EXPOSE 3000  
ENV NODE_ENV=production  
RUN apk update  
RUN apk add libcap libcec  
RUN setcap "CAP_NET_RAW+eip CAP_NET_ADMIN+eip" $(which node)  
WORKDIR /var/www/homeautomation  
COPY \--from=builder /var/www/homeautomation/ .  
  
CMD ["npm", "start"]  

