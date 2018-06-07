#put together a HLS streaming image based on alpine linux and ffmpeg  
FROM alpine  
RUN apk update && apk add nginx fcgiwrap ffmpeg  
RUN mkdir -p /opt/video && ffmpeg -f lavfi -i "testsrc=size=2k" -pix_fmt
yuv420p -t 10 /opt/video/testsrc.mp4  
COPY etc /etc/  
COPY root /root/  
COPY htdocs /var/www/localhost/htdocs/  
EXPOSE 80  
RUN mkdir -p /run/nginx && chmod a+x /root/start.sh && chmod a+x
/var/www/localhost/htdocs/cgi/*  
RUN chown -R root:www-data /var/www/  
CMD /root/start.sh  

