FROM alpine  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
RUN mkdir /app && \  
adduser -h /app -s /bin/false -D app && \  
chown -R app:app /app && \  
apk update && \  
apk add --no-cache nodejs && \  
rm -f /tmp/* /etc/apk/cache/* && \  
npm update && \  
npm i -g typescript tslint alm  
  
USER app  
ENV HOME=/app  
WORKDIR $HOME  
  
ENTRYPOINT ["alm"]  
CMD ["--version"]  

