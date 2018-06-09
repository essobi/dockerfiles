FROM fluent/fluentd:v1.0  
USER root  
WORKDIR /home/fluent  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
ruby-dev \  
libffi-dev \  
&& echo 'gem: --no-document' >> /etc/gemrc \  
&& gem install fluent-plugin-secure-forward \  
&& gem install fluent-plugin-record-reformer \  
&& gem install fluent-plugin-mongo \  
&& gem install fluent-plugin-kubernetes_metadata_filter \  
&& apk del .build-deps \  
&& gem sources --clear-all \  
&& rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem  
  
# Create directory to store fluentd pos files.  
RUN mkdir -p /home/fluent/pos  
  
# Copy configuration files  
COPY ./conf/fluent.conf /fluentd/etc/  
COPY ./conf/kubernetes.conf /fluentd/etc/  
  
# Copy plugins  
COPY plugins /fluentd/plugins/  
  
# Environment variables  
ENV FLUENTD_OPT=""  
ENV FLUENTD_CONF="fluent.conf"  
# Run Fluentd  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT

