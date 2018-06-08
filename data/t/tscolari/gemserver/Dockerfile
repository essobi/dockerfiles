FROM alpine  
MAINTAINER Tiago Scolari <tscolari@gmail.com>  
  
RUN apk update &&\  
apk add ruby \  
ruby-bundler \  
linux-headers \  
ca-certificates &&\  
apk add --virtual build-dependencies \  
build-base \  
ruby-dev \  
libressl-dev &&\  
rm -rf /usr/lib/ruby/gems/*/cache/* \  
/var/cache/apk/* \  
/tmp/* \  
/var/tmp/*  
  
RUN mkdir /var/gems  
RUN mkdir /geminabox  
  
VOLUME /var/gems  
  
ADD Gemfile ./geminabox/  
ADD Gemfile.lock ./geminabox/  
ADD config.ru ./geminabox/  
ADD unicorn.rb ./geminabox/  
WORKDIR /geminabox  
RUN bundle install  
  
ENV PORT 6444  
CMD ["bundle", "exec", "unicorn", "-c", "/geminabox/unicorn.rb"]  

