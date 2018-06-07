FROM alpine:latest  
MAINTAINER Andrew Taranik <me@pureclouds.net>  
  
ENV AGE 7  
ENV INDEX logstash  
ENV ELASTICSEARCH_HOST elasticsearch  
ENV ELASTICSEARCH_PORT 9200  
RUN apk --no-cache add \  
tini \  
python \  
py-setuptools \  
py-pip \  
gettext \  
&& pip install elasticsearch-curator \  
&& cp /usr/bin/envsubst /usr/local/bin/ \  
&& apk --no-cache del \  
py-pip \  
&& apk --no-cache add \  
libintl  
  
RUN echo '#!/bin/sh' | tee /etc/periodic/daily/curator \  
&& echo 'curator --config /config.yml /actions.yml' | tee -a
/etc/periodic/daily/curator \  
&& chmod +x /etc/periodic/daily/curator  
  
ADD config.yml.tmpl /config.yml.tmpl  
ADD actions.yml.tmpl /actions.yml.tmpl  
ADD init.sh /init.sh  
  
ENTRYPOINT ["/sbin/tini", "--"]  
  
CMD ["/init.sh"]  

