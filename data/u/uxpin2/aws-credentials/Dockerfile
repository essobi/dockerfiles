FROM ruby:2.3-alpine  
  
WORKDIR /app  
  
RUN gem install bundler  
  
RUN apk add --update \  
build-base \  
libxml2-dev \  
libxslt-dev \  
tzdata \  
&& rm -rf /var/cache/apk/*  
  
RUN bundle config build.nokogiri --use-system-libraries  
  
ADD Gemfile Gemfile.lock ./  
RUN bundle install  
  
ADD . ./  
EXPOSE 3000  
CMD ["./bin/rails", "server"]  

