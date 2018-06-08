FROM alpine:3.6  
ADD shot.sh /shot.sh  
RUN apk --update --no-cache add ffmpeg && rm -rf /var/cache/apk/* && mkdir
/tmp/cam-data  
VOLUME ["/tmp/cam-data"]  
CMD ["/shot.sh"]  

