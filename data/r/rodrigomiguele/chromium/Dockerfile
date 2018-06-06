FROM alpine  
  
RUN apk add \--update chromium libexif udev && \  
apk info \--purge  
  
RUN addgroup developer && adduser developer -G developer -h /home/developer -D  
RUN delgroup audio && addgroup audio -g 29 && addgroup developer audio  
USER developer  
WORKDIR /home/developer/  
  
ENTRYPOINT ["chromium-browser"]  

