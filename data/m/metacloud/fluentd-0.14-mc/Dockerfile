FROM alpine:3.5  
MAINTAINER David Pippenger <riven@particle-man.com>  
LABEL Description="Fluentd docker image" Vendor="Particle-man Organization"
Version="1.2"  
  
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
&& gem install fluentd -v 0.14.21 \  
&& gem install fluent-plugin-elasticsearch -v 1.10.0 \  
&& gem install fluent-plugin-record-reformer -v 0.9.1 \  
&& gem install fluent-plugin-rewrite-tag-filter -v 1.5.6 \  
&& gem install fluent-plugin-tcp_mc -v 0.1.0 \  
&& gem install fluent-plugin-multi-format-parser -v 0.1.1 \  
&& gem sources --clear-all \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem  
  
RUN adduser -D -g '' -u 1000 -h /home/fluent fluent  
RUN chown -R fluent:fluent /home/fluent  
  
# for log storage (maybe shared with host)  
RUN mkdir -p /fluentd/log  
# configuration/plugins path (default: copied from .)  
RUN mkdir -p /fluentd/etc /fluentd/plugins  
  
RUN chown -R fluent:fluent /fluentd  
  
USER fluent  
WORKDIR /home/fluent  
  
# Tell ruby to install packages as user  
RUN echo "gem: --user-install --no-document" >> ~/.gemrc  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
ENV GEM_PATH /home/fluent/.gem/ruby/2.3.0:$GEM_PATH  
  
COPY fluent.conf /fluentd/etc/  
ONBUILD COPY fluent.conf /fluentd/etc/  
ONBUILD COPY plugins /fluentd/plugins/  
  
ENV FLUENTD_OPT=""  
ENV FLUENTD_CONF="fluent.conf"  
ENV LD_PRELOAD=""  
EXPOSE 24224 5140  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT  

