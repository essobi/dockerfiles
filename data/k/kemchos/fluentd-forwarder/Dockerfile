FROM alpine:latest  
  
RUN apk --update add ruby ruby-json ruby-bigdecimal ruby-irb ruby-rake ruby-
io-console \  
&& rm -rf /var/cache/apk/*  
  
RUN apk --update add --virtual build-dev build-base ruby-dev \  
&& echo "gem: --no-ri --no-rdoc" > ~/.gemrc \  
&& gem install fluentd \  
&& gem install fluent-plugin-record-reformer \  
&& gem install docker-api \  
&& mkdir -p /etc/fluent/plugin \  
&& fluentd --setup /etc/fluent \  
&& apk del build-dev \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
EXPOSE 24220  
COPY ./fluent.conf /etc/fluent/fluent.conf  
COPY ./plugin /etc/fluent/plugin  
  
ENTRYPOINT ["/usr/bin/fluentd"]  
CMD ["-c", "/etc/fluent/fluent.conf", "-p", "/etc/fluent/plugin"]

