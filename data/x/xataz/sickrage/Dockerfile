FROM xataz/alpine:3.3  
MAINTAINER xataz <https://github.com/xataz>  
  
ENV WEBROOT="/" \  
UID="991" \  
GID="991"  
RUN apk add -U python \  
py-pip \  
git \  
&& pip install cheetah \  
&& git clone https://github.com/SickRage/SickRage.git \  
&& apk del py-pip \  
&& rm -rf /var/cache/apk/*  
  
ADD startup /usr/bin/startup  
ADD config.ini /tmp/config.ini  
RUN chmod +x /usr/bin/startup  
  
VOLUME ["/config"]  
EXPOSE 8081  
CMD ["tini","--","/usr/bin/startup"]  

