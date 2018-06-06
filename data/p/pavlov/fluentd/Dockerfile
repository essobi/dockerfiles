FROM alpine:3.4  
MAINTAINER Alex Kern <alex@pavlov.ai>  
  
RUN apk --no-cache --update add \  
build-base \  
ca-certificates \  
ruby \  
ruby-irb \  
ruby-dev && \  
echo 'gem: --no-document' >> /etc/gemrc && \  
gem install oj && \  
gem install json && \  
gem install fluentd -v 0.14.9 && \  
gem install fluent-plugin-s3 && \  
gem install fluent-plugin-loggly && \  
gem install fluent-plugin-kubernetes_metadata_filter && \  
apk del build-base ruby-dev && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/* && \  
mkdir -p /etc/fluent  
  
WORKDIR /etc/fluent  
COPY fluent.conf .  
  
EXPOSE 24220  
CMD [ "fluentd", "-c", "fluent.conf" ]  

