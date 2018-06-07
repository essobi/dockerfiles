FROM alpine  
  
RUN apk update && apk upgrade \  
&& apk add nodejs python make g++ \  
&& npm update -g npm \  
&& npm install -g log.io --user 'root' \  
&& apk del python make g++ \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 28777 28778  
VOLUME [ "/var/log" ]  
  
COPY harvester.conf /root/.log.io/harvester.conf  
COPY entry.sh /usr/local/bin  
CMD [ "entry.sh" ]  

