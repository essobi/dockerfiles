FROM xataz/alpine:3.3  
MAINTAINER xataz <https://github.com/xataz>  
  
LABEL description="sickrage based on alpine"  
  
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
  
COPY startup /usr/bin/startup  
COPY config.ini /tmp/config.ini  
RUN chmod +x /usr/bin/startup  
  
VOLUME ["/config"]  
EXPOSE 8081  
CMD ["tini","--","/usr/bin/startup"]  

