FROM alpine:3.4  
ENV SYSTEM_PKGS bash build-base cmake curl git wget libffi-dev  
ENV RUBY_PKGS ruby-dev ruby ruby-bigdecimal ruby-bundler  
  
RUN apk update && \  
apk upgrade && \  
apk add $SYSTEM_PKGS && \  
apk add $RUBY_PKGS && \  
rm -rf /var/cache/apk/*  
  
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc  
RUN echo 'gem: --no-document' >> ~/.gemrc  
  
RUN gem install bundler  

