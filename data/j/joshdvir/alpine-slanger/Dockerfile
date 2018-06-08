FROM ruby:2-alpine  
  
RUN apk add --update \  
bash \  
build-base \  
&& gem install slanger --no-rdoc --no-ri \  
&& apk del --update build-base \  
&& rm -rf /var/cache/apk/*  
  
RUN gem install slanger  
  
COPY start.sh /tmp/start.sh  
  
ENTRYPOINT ["/tmp/start.sh"]

