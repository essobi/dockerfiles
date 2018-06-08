FROM fluent/fluentd:latest  
MAINTAINER Tokyo HOME SOC <github@homesoc.tokyo>  
  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
# Environment variable  
ARG TIMEZONE=Asia/Tokyo  
  
USER root  
WORKDIR /home/fluent  
  
RUN \  
apk add --no-cache --virtual .build-tzdata \  
tzdata \  
&& cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \  
&& apk del .build-tzdata \  
&& apk add --no-cache \  
curl \  
bash \  
&& apk add --no-cache --virtual .build-gem \  
git \  
ruby-dev \  
build-base \  
libcurl \  
&& chown -R fluent:fluent /fluentd/etc/ \  
\  
&& gem install fluent-plugin-s3 --no-ri --no-rdoc \  
&& gem install fluent-plugin-slack --no-ri --no-rdoc \  
&& gem install fluent-plugin-norikra --no-ri --no-rdoc \  
&& gem install fluent-plugin-suppress --no-ri --no-rdoc \  
&& gem install fluent-plugin-elasticsearch --no-ri --no-rdoc \  
&& apk del .build-gem  
  
COPY /conf.d /fluentd/etc/conf.d/  
COPY /fluent.conf /docker-entrypoint.sh /fluentd/etc/  
COPY /mapping /fluentd/etc/mapping/  
  
ENTRYPOINT [ "/fluentd/etc/docker-entrypoint.sh" ]  
USER fluent  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT

