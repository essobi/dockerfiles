FROM fluent/fluentd:v1.1.2  
USER root  
WORKDIR /home/fluent  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
ruby-dev \  
libffi-dev \  
&& echo 'gem: --no-document' >> /etc/gemrc \  
&& gem install aws-sdk-core -v 3.18.1 \  
&& gem install aws-sdk-cloudwatchlogs -v 1.2.0 \  
&& gem install fluent-plugin-cloudwatch-logs -v 0.4.5 \  
&& gem install fluent-plugin-kubernetes_metadata_filter -v 1.0.1 \  
&& gem install fluent-plugin-prometheus -v 1.0.1 \  
&& gem install fluent-plugin-rewrite-tag-filter -v 2.0.2 \  
&& gem install ffi -v 1.9.23 \  
&& gem install fluent-plugin-systemd -v 0.3.1 \  
&& gem install fluent-plugin-datacounter -v 1.0.0 \  
&& apk del .build-deps \  
&& gem sources --clear-all \  
&& rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem  
  
# Run Fluentd  
ENTRYPOINT [ "fluentd", "-p", "/fluentd/plugins", "-c",
"/etc/fluentd/fluent.conf" ]  

