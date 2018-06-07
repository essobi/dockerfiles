FROM alpine:latest  
  
MAINTAINER Peter Szalatnay <theotherland@gmail.com>  
  
# Define Joomla version and expected SHA1 signature  
ENV JOOMLA_VERSION=3.5.1 #JOOMLA_SHA1=  
RUN \  
addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& apk add --update \  
curl \  
&& rm -fr /var/cache/apk/* \  
&& curl -o joomla.zip -SL https://github.com/joomla/joomla-
cms/releases/download/${JOOMLA_VERSION}/Joomla_${JOOMLA_VERSION}-Stable-
Full_Package.zip \  
#&& echo "$JOOMLA_SHA1 *joomla.zip" | sha1sum -c - \  
&& mkdir -p /data/html \  
&& unzip joomla.zip -d /data/html \  
&& rm joomla.zip  
  
COPY ./docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh  
  
VOLUME ["/usr/share/nginx/html"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

