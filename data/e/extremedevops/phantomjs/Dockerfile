FROM debian:jessie  
MAINTAINER Leandro David Cacciagioni <leandro.21.2008@gmail.com>  
  
EXPOSE 6000  
VOLUME /var/phantomjs_storage  
  
CMD phantomjs --webdriver=6000 --disk-cache=true \--cookies-
file=/tmp/cookies.txt --load-images=true \--max-disk-cache-size=524288
--local-storage-path=/var/phantomjs_storage  
  
ADD build /build  
  
RUN chmod 0755 /build && sleep 1 && /build  

