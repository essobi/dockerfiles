FROM node:6-alpine  
  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh shadow su-exec  
  
RUN npm install --global --silent yo  
  
ENV LANG en_US.UTF-8  
RUN mkdir /generated  
WORKDIR /generated  
  
ADD entrypoint.sh /usr/local/sbin/  
RUN chmod +x /usr/local/sbin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]

