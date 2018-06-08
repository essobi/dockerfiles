FROM alpine  
LABEL maintainer "marc@malexandre.fr"  
  
RUN apk update && apk add nodejs git openssh-client && rm -rf /var/cache/apk/*  
RUN npm install -g bower gulp  
  
WORKDIR /code  

