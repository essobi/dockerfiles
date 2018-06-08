FROM alpine:3.4  
MAINTAINER nownabe  
  
ENV build_deps "build-base ruby-dev"  
RUN apk add --no-cache --update ${build_deps} \  
&& apk add --no-cache --update ruby ruby-irb ca-certificates \  
&& gem install json --no-document -v "2.0.2" \  
&& gem install oj --no-document -v "2.17.5" \  
&& gem install fluentd --no-document -v "0.14.8" \  
&& apk del ${build_deps} \  
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /usr/lib/ruby/gems/*/cache/*.gem
\  
&& mkdir -p /etc/fluent/plugins /etc/fluent/conf.d  
  
COPY ./fluent.conf /etc/fluent/  
  
ENV FLUENTD_OPTS=""  
ENV FLUENTD_CONF="/etc/fluent/fluent.conf"  
  
CMD /usr/bin/fluentd -c $FLUENTD_CONF -p /etc/fluent/plugins $FLUENTD_OPTS  

