FROM fluent/fluentd:v0.12.34  
MAINTAINER Ruslan Lutsenko <rlutsenko@travix.com>  
USER root  
WORKDIR /home/fluent  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
ruby-dev \  
&& echo 'gem: --no-document' >> /etc/gemrc \  
&& gem install fluent-plugin-flowcounter \  
&& gem install fluent-plugin-prometheus \  
&& apk del .build-deps \  
&& rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem  
  
# Copy configuration files  
COPY ./conf/fluent.conf /fluentd/etc/  
  
# Environment variables  
ENV FLUENTD_OPT=""  
ENV FLUENTD_CONF="fluent.conf"  
# jemalloc is memory optimization only available for td-agent  
# td-agent is provided and QA'ed by treasuredata as rpm/deb/.. package  
# -> td-agent (stable) vs fluentd (edge)  
#ENV LD_PRELOAD="/usr/lib/libjemalloc.so.2"  
# Run Fluentd  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF $FLUENTD_OPT  

