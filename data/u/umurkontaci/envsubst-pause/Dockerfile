FROM alpine:3.5  
ADD pause.c /src/pause.c  
RUN apk add --update gettext build-base && \  
cd /src && gcc pause.c -o pause && \  
mv pause /usr/bin/pause && \  
chmod +x /usr/bin/pause && \  
apk del build-base && \  
rm -rf /src  
  
ADD start.sh /start.sh  
ENTRYPOINT ["/start.sh"]  

