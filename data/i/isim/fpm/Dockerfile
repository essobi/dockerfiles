FROM ruby:2.3.0-alpine  
MAINTAINER Ivan Sim "ihcsim@gmail.com"  
RUN apk add --update ruby-dev gcc make musl-dev libffi-dev xz-dev tar && \  
gem install fpm  
ENTRYPOINT ["fpm"]  
CMD ["--help"]  

