FROM alpine:3.6  
MAINTAINER devops@razorpay.com  
LABEL Description="Fluentd docker image for splunk as output"  
  
ENV DUMB_INIT_VERSION=1.2.0  
ENV SU_EXEC_VERSION=0.2  
  
COPY entrypoint.sh /bin/  
  
WORKDIR /home/fluent  
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH  
  
# for log storage (will be mounted with the host where trace|nginx logs are
mounted)  
RUN mkdir -p /fluentd/log \  
&& mkdir -p /fluentd/etc /fluentd/plugins \  
&& apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
ca-certificates \  
ruby ruby-irb \  
su-exec==${SU_EXEC_VERSION}-r0 \  
dumb-init==${DUMB_INIT_VERSION}-r0 \  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
ruby-dev wget gnupg \  
&& update-ca-certificates \  
&& echo 'gem: --no-rdoc --no-ri ' >> /etc/gemrc \  
&& gem install oj -v 2.18.3 \  
&& gem install json -v 2.1.0 \  
&& gem install fluentd -v 0.12.39 \  
&& gem install fluent-plugin-splunk-http-eventcollector \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem \  
&& chmod +x /bin/entrypoint.sh  
  
  
# Environment variables  
ENV FLUENTD_CONF="splunk.conf"  
COPY ./conf/${FLUENTD_CONF} /fluentd/etc/  
  
ENTRYPOINT ["/bin/entrypoint.sh"]  
  
CMD fluentd -c /fluentd/etc/${FLUENTD_CONF} -p /fluentd/plugins  

