# docker build -t ptimof/ghost .  
#  
# Build from the official release  
FROM ghost:1.14.0-alpine  
  
LABEL maintainer Tim Friedrich <info@jimtim.de>  
# Default environment variables  
ENV URL http://my-ghost-blog.com  
ENV MAIL__FROM '<hallo@example.com>'  
ENV MAIL__OPTIONS__HOST smtp-relay.example.com  
ENV USEMINFILES true  
  
COPY config.production.example.json config.production.example.json  
COPY env-defaults.sh /env-defaults.sh  
COPY docker-entrypoint.sh /usr/local/bin  
RUN dos2unix /env-defaults.sh \  
&& dos2unix /usr/local/bin/docker-entrypoint.sh \  
&& dos2unix config.production.example.json \  
&& apk add --no-cache bash && chmod +x /env-defaults.sh && chmod +x
/usr/local/bin/docker-entrypoint.sh  
  

