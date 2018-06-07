FROM ruby:2.3-alpine  
MAINTAINER Firespring "info.dev@firespring.com"  
RUN mkdir /root/.gemstash  
  
RUN apk add --update ca-certificates sqlite-libs \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
RUN apk --update add --virtual build-dependencies ruby-dev build-base sqlite-
dev \  
&& gem install --no-rdoc --no-ri gemstash \  
&& apk del build-dependencies \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["gemstash"]  
EXPOSE 9292  
CMD ["start", "--no-daemonize"]  

