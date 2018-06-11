FROM alpine:latest  
MAINTAINER Sean Hsu <sahsu.mobi@gmail.com>  
EXPOSE 80  
ENV HOME=/root  
  
# install packages  
RUN apk --update --no-progress add php php-xml php-dom openssl wget\  
&& rm -rf /var/cache/apk/*  
  
# install s6 supervisor  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && rm /tmp/s6-overlay-
amd64.tar.gz  
CMD ["/init"]  
  
COPY phpsysinfo.s6 /etc/services.d/phpsysinfo/run  
COPY beforeRun.sh /beforeRun.sh  
  
RUN /beforeRun.sh  

