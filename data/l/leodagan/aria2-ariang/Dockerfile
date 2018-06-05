FROM alpine:edge  
  
MAINTAINER Leodagan <leodagan@freyad.net>  
  
RUN apk update && \  
apk add --no-cache --update bash && \  
apk add --no-cache --update aria2 && \  
apk add --no-cache --update nginx && \  
apk add --no-cache --update unzip && \  
apk add --no-cache --update openssl && \  
aria2c "https://github.com/mayswind/AriaNg-DailyBuild/archive/master.zip" -d /
&& \  
# aria2c "https://github.com/mayswind/AriaNg/releases/download/0.2.0/aria-
ng-0.2.0.zip" -d / && \  
unzip /*.zip -d /aria-ng && \  
mv -n "$(dirname "$(find /aria-ng -name "index.html")")"/* /aria-ng && \  
rm -f /*.zip && \  
apk del unzip && \  
echo "pid /nginx.pid;" >> /etc/nginx/nginx.conf  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ADD on_download_complete.sh /on_download_complete.sh  
RUN chmod +x /on_download_complete.sh  
  
ADD default.conf /etc/nginx/conf.d/default.conf  
ADD default-unsecure.conf /default-unsecure.conf  
ADD aria2.conf /root/.aria2/aria2.conf  
  
WORKDIR /  
VOLUME ["/data"]  
VOLUME ["/conf"]  
EXPOSE 80 443  
CMD ["/entrypoint.sh"]  

