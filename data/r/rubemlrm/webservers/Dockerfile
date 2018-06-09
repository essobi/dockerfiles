FROM alpine:latest  
MAINTAINER Rubem Mota <rubemmota89@gmail.com>  
  
#update system and install needed packages  
ADD https://github.com/tianon/gosu/releases/download/1.9/gosu-armhf
/usr/sbin/gosu  
RUN chmod +x /usr/sbin/gosu \  
&& echo "http://dl-4.alpinelinux.org/alpine/v3.3/main/" | tee
/etc/apk/repositories \  
&& echo "http://dl-4.alpinelinux.org/alpine/v3.3/community/" | tee -a
/etc/apk/repositories \  
&& apk -U --no-progress upgrade && rm -f /var/cache/apk/APKINDEX.* \  
&& apk --no-cache --no-progress add ca-certificates nginx curl bash  
  
#copy conf files  
COPY conf/nginx.conf /etc/nginx/nginx.conf  
COPY conf/sites/ /etc/nginx/conf.d/  
EXPOSE 80  
CMD ["nginx"]  
  

