FROM existenz/base  
  
MAINTAINER docker@stefan-van-essen.nl  
  
RUN apk -U add rtorrent && rm -rf /var/cache/apk/* && mkdir /home/session  
  
ENTRYPOINT ["runas", "rtorrent"]  

