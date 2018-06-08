FROM alpine:3.3  
MAINTAINER ninthwalker <ninthwalker@gmail.com>  
  
VOLUME /config  
EXPOSE 6878  
  
ENV BUILD_PACKAGES bash curl-dev ruby-dev  
#ENV RUBY_PACKAGES  
ENV BUNDLER_VERSION 1.12.3  
  
#copy nowShowing files  
COPY root/ /  
WORKDIR /opt/gem  
  
RUN apk add \--update \  
$BUILD_PACKAGES \  
ruby \  
ruby-io-console \  
ruby-json \  
make \  
gcc  
#ruby-irb  
#ruby-rake  
#ruby-rdoc  
# $RUBY_PACKAGES \  
# may need build-base (includes make, gcc and others, but is large (like
100mb)  
RUN gem install bundler -v $BUNDLER_VERSION \--no-ri --no-rdoc  
RUN bundle config \--global silence_root_warning 1  
RUN bundle install  
  
CMD ["ruby", "-run", "-e", "httpd", ".", "-p", "6878"]  

