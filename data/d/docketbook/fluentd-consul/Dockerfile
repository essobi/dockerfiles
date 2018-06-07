FROM fluent/fluentd:latest  
MAINTAINER Dave Finster <df@docketbook.io>  
  
ENV CONTAINERBUDDY_VERSION 1.2.1  
  
COPY fluentd-consul.json /etc/fluentd-consul.json  
COPY fluent_health.sh /usr/local/bin/fluent_health.sh  
  
USER root  
  
RUN set -x \  
&& apk add --no-cache --virtual .build-deps \  
openssl \  
&& wget -O containerbuddy.tar.gz
https://github.com/joyent/containerbuddy/releases/download/"$CONTAINERBUDDY_VERSION"/containerbuddy-"$CONTAINERBUDDY_VERSION".tar.gz
\  
&& tar -xzf containerbuddy.tar.gz -C /usr/local/bin \  
&& rm -r containerbuddy.tar.gz \  
&& apk del .build-deps \  
&& chmod +x /usr/local/bin/fluent_health.sh  
  
USER fluent  
  
ENV CONTAINERBUDDY=file:///etc/fluentd-consul.json  
  
EXPOSE 24224  
  
ENTRYPOINT [ "/usr/local/bin/containerbuddy", "/usr/bin/fluentd", "-c",
"/fluentd/etc/fluent.conf"]

