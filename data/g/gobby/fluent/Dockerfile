FROM alpine:latest  
MAINTAINER Radoslaw 'Goblin' Pieczonka <goblin@pentex.pl>  
  
RUN apk update; apk add ruby ruby-dev ruby-irb build-base ;\  
gem install json ;\  
gem install fluentd --no-ri --no-rdoc ;\  
fluentd --setup ;\  
gem install fluent-plugin-secure-forward ;\  
apk del ruby-dev build-base  
  
CMD ["fluentd"]  
  

