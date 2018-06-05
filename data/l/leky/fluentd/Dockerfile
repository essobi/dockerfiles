FROM leky/ruby:latest  
MAINTAINER leky <lekyzsj@gmail.com>  
  
ENV FLUENTD_OPTIONS="" \  
FLUENTD_CONFIG="fluent.conf"  
  
RUN apk add --no-cache --virtual .fluentBuildDeps build-base \  
&& gem install fluentd --no-ri --no-rdoc \  
&& apk del .fluentBuildDeps  
  
RUN addgroup fluent && adduser -D -h /home/fluent -G fluent fluent  
  
# For log storage, configuration and plugins.  
RUN mkdir -p /var/lib/fluentd/log \  
&& mkdir -p /var/lib/fluentd/conf \  
&& mkdir -p /var/lib/fluentd/plugins \  
&& chown -R fluent:fluent /var/lib/fluentd  
  
USER fluent  
WORKDIR /home/fluent  
  
ADD ${FLUENTD_CONFIG} /fluentd/conf/  
  
EXPOSE 24224 5140  
  
CMD fluentd -c /var/lib/fluentd/conf/${FLUENTD_CONFIG} -p
/var/lib/fluentd/plugins ${FLUENTD_OPTIONS}  

