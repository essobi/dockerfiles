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
&& chown -R fluent:fluent /fluentd/etc/ \  
\  
&& gem install specific_install \  
&& gem specific_install -l 'git://github.com/tokyohomesoc/fluent-plugin-
elasticsearch-jvm.git' \  
&& gem install specific_install \  
&& gem specific_install -l 'git://github.com/tokyohomesoc/fluent-plugin-
jvm.git' \  
&& gem install fluent-plugin-slack --no-ri --no-rdoc \  
&& gem install fluent-plugin-suppress --no-ri --no-rdoc \  
&& gem install fluent-plugin-mackerel --no-ri --no-rdoc \  
&& gem install fluent-plugin-s3 --no-ri --no-rdoc \  
&& apk del .build-gem  
  
COPY /conf.d /fluentd/etc/conf.d/  
COPY /fluent.conf /fluentd/etc/  
  
USER fluent  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT

