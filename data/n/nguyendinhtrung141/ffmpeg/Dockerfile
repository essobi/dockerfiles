FROM alpine:latest  
MAINTAINER Trung Nguyen <nguyendinhtrung141@gmail.com>  
  
RUN apk --no-cache add ffmpeg ffmpegthumbnailer perl  
ADD ./rename.pl /usr/local/sbin/rename.pl  
ENTRYPOINT ash  

