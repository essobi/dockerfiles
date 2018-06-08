FROM alpine:edge  
MAINTAINER Sebastian Knoth <sebastian.knoth@gmail.com>  
  
WORKDIR /tmp  
  
# Add CURL and required php7 extensions  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
nodejs  
  
RUN rm -fr /var/cache/apk/*  
  
WORKDIR /usr/share/nginx/html  
  
CMD ["npm", "start"]

