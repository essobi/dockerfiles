FROM alpine:3.3  
MAINTAINER jonadup <jonathan.dupuich@gmail.com>  
  
  
RUN apk update && apk upgrade && apk --update add \  
ruby ruby-irb ruby-rake ruby-io-console ruby-bigdecimal \  
libstdc++ tzdata bash openssh  
  
RUN echo 'gem: --no-rdoc --no-ri' > /etc/gemrc  
RUN gem install capistrano highline airbrussh  
RUN mkdir /root/cap  
WORKDIR /root/cap  

