FROM python:2-alpine  
MAINTAINER RWd <rwd-github@gmx.net>  
  
RUN apk add --no-cache --update nodejs make g++  
  
RUN npm install ethercalc && \  
ln -s ../../node_modules /node_modules/ethercalc/node_modules  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

