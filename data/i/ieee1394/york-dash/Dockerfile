FROM ruby:2.4.3-alpine  
EXPOSE 5001  
ENV BUILD_PACKAGES bash curl-dev build-base git nodejs  
ENV RUBY_PACKAGES libxml2-dev libxslt-dev  
  
# Update and install all of the required packages.  
# At the end, remove the apk cache  
RUN apk update && \  
apk upgrade && \  
apk add $BUILD_PACKAGES && \  
apk add $RUBY_PACKAGES && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir /usr/app  
WORKDIR /usr/app  
  
COPY Gemfile /usr/app/  
COPY Gemfile.lock /usr/app/  
  
RUN gem install bundler  
RUN bundle install  
  
COPY . /usr/app  
  
# Default server command  
CMD ["bash", "/usr/app/server.sh"]  

