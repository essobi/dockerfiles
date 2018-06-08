FROM alpine:3.7  
RUN apk update && apk --no-cache add git mediainfo su-exec python2 \  
&& git clone \--depth=1 https://github.com/pymedusa/Medusa.git /opt/ \  
&& mkdir config tv downloads \  
&& rm -r /var/cache/apk/*  
COPY . /  
EXPOSE 8081  
VOLUME /config  
ENTRYPOINT ["/entrypoint.sh"]  

