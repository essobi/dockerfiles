FROM alpine:latest  
MAINTAINER gtclai <tsungchih.hd@gmail.com>  
  
RUN apk --no-cache --update add \  
build-base \  
ca-certificates \  
ruby \  
ruby-irb \  
ruby-dev && \  
echo 'gem: --no-document' >> /etc/gemrc && \  
gem install oj && \  
gem install fluentd -v 0.12.24 && \  
gem install fluent-plugin-kafka -v 0.1.4 && \  
apk del build-base ruby-dev && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/*  
  
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
ENV PATH /home/fluent/.gem/ruby/2.2.0/bin:$PATH  
ENV GEM_PATH /home/fluent/.gem/ruby/2.2.0:$GEM_PATH  
  
COPY fluent.conf /fluentd/etc/  
ONBUILD COPY fluent.conf /fluentd/etc/  
ONBUILD COPY plugins /fluentd/plugins/  
  
ENV FLUENTD_OPT=""  
ENV FLUENTD_CONF="fluent.conf"  
EXPOSE 24220 24224 5140  
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins
$FLUENTD_OPT  

