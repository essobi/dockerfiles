FROM bandsintown/alpine:3.5  
MAINTAINER Bandsintown Devops Team "devops@bandsintown.com"  
# Do not split this into multiple RUN!  
# Docker creates a layer for every RUN-Statement  
# therefore an 'apk delete' has no effect  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
ca-certificates \  
ruby ruby-irb \  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
ruby-dev \  
&& update-ca-certificates \  
&& echo 'gem: --no-document' >> /etc/gemrc \  
&& gem install oj \  
&& gem install json \  
&& gem install fluentd -v 0.12.32 \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem  
  
# for log storage (maybe shared with host)  
RUN mkdir -p /fluentd/log  
# configuration/plugins path (default: copied from .)  
RUN mkdir -p /fluentd/etc /fluentd/plugins  
  
COPY fluent.conf /fluentd/etc/  
  
ENV FLUENTD_OPT=""  
ENV FLUENTD_CONF="fluent.conf"  
ENV LD_PRELOAD=""  
EXPOSE 24224 5140  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT

