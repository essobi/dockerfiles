FROM alpine:3.6  
COPY ./janus-pp-rec /usr/local/bin/janus-pp-rec  
COPY ./convert-mjr-to-mp4.sh /usr/local/bin/mjr2mp4  
RUN apk update && apk add glib ffmpeg jansson && chmod a+x
/usr/local/bin/mjr2mp4 && rm -rf /var/cache/apk/*  
ENTRYPOINT ["mjr2mp4"]  
  

