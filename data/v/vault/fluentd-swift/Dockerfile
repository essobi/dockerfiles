FROM alpine:3.5  
MAINTAINER Christoph Dwertmann <christoph.dwertmann@vaultsystems.com.au>  
RUN apk --update add ruby ruby-dev ruby-irb libxslt libxml2 curl  
COPY *.gem /  
RUN apk --update add --virtual build-dependencies build-base libxml2-dev
libxslt-dev \  
&& echo ":ssl_verify_mode: 0" > ~/.gemrc \  
&& gem install fluentd fluent-plugin-record-reformer fluent-plugin-swift
fluent-plugin-parser fluent-plugin-fortigate-log-parser fluent-plugin-
elasticsearch fluent-plugin-multiprocess io-console fog excon --no-rdoc --no-
ri -- --use-system-libraries \  
&& apk del build-dependencies \  
&& rm /etc/localtime \  
&& rm /var/cache/apk/*  
RUN mkdir /etc/fluent  
CMD ["fluentd","-c","/etc/fluent/fluent.conf"]  

