FROM alpine:3.6  
MAINTAINER Denis Chekirda <dchekirda@gmail.com>  
LABEL Description="Alpine Based FluentD container with preinstalled
Elasticsearhc, Forest, Logzio plugins"  
  
RUN apk --update \--no-cache add ruby ruby-dev ruby-json ruby-irb build-base
ca-certificates &&\  
rm -rf /var/cache/apk &&\  
gem install fluentd --no-ri \--no-document &&\  
gem install fluent-plugin-elasticsearch --no-ri \--no-document &&\  
gem install fluent-plugin-forest --no-ri \--no-document &&\  
gem install fluent-plugin-logzio --no-ri \--no-document &&\  
apk del build-base ruby-dev &&\  
rm -rf /root/.gem  
  
COPY config/fluentd.conf /etc/fluent/fluent.conf  
EXPOSE 24224  
  
CMD ["/usr/bin/fluentd"]  

