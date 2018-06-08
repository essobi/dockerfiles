FROM ruby:2.3-alpine  
  
MAINTAINER Reputation VIP <it@reputationvip.com>  
  
RUN gem install scss_lint  
  
VOLUME ["/app"]  
  
WORKDIR /app  
  
ENTRYPOINT ["scss-lint"]  

