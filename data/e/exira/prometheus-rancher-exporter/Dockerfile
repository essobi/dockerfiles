FROM exira/base:latest  
  
MAINTAINER exira.com <info@exira.com>  
  
RUN \  
# Install build and runtime packages  
runtime_pkgs="nodejs" && \  
apk update && \  
apk upgrade && \  
apk --update --no-cache add ${runtime_pkgs} && \  
  
# other clean up  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/* && \  
rm -rf /var/log/*  
  
WORKDIR /app  
  
ADD app.js /app/  
ADD package.json /app/  
RUN npm install  
  
ENV DEBUG re  
EXPOSE 9010  
CMD ["npm", "start"]  

