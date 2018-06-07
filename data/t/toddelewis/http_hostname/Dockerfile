FROM node:6.10.0-alpine  
  
RUN mkdir /usr/local/node \  
&& addgroup -g 5000 nodejs \  
&& adduser -u 5000 -G nodejs -H -s /bin/ash nodejs \  
&& find / -perm /6000 -type f -exec chmod a-s {} \; || true  
  
COPY http_hostname.js /usr/local/node  
USER nodejs  
  
EXPOSE 1337  
CMD node /usr/local/node/http_hostname.js && tail -f /dev/null  

