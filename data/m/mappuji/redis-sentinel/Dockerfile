FROM redis:4.0.8-alpine  
  
MAINTAINER Abdurrachman Mappuji <hi@mappuji.org>  
  
ENV SENTINEL_QUORUM 1  
ENV SENTINEL_DOWN_AFTER 30000  
ENV SENTINEL_FAILOVER 180000  
WORKDIR /sentinel  
ADD . /sentinel  
RUN apk add --no-cache \  
curl \  
bash \  
gettext libintl \  
netcat-openbsd \  
&& mv sentinel-entrypoint.sh /usr/local/bin/sentinel-entrypoint.sh \  
&& chmod +x /usr/local/bin/sentinel-entrypoint.sh  
  
ENTRYPOINT ["sentinel-entrypoint.sh"]

