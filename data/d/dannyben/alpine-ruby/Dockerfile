FROM alpine:3.7  
ENV BUILD_PACKAGES bash curl curl-dev ruby-dev build-base  
ENV RUBY_PACKAGES ruby ruby-io-console ruby-irb ruby-json libffi-dev zlib-dev
ruby-bigdecimal  
ENV TERM=linux  
ENV PS1 "\n\n>> ruby \W \$ "  
RUN apk --no-cache add $BUILD_PACKAGES $RUBY_PACKAGES  
  
RUN echo 'gem: --no-document' > /etc/gemrc && \  
gem install bundler  
  
RUN bundle config --global silence_root_warning 1  
  
CMD bash

