FROM ruby:2.5.1-alpine  
  
RUN apk add --no-cache \  
build-base \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /usr/local/lib/ruby/gems/*/cache/* \  
&& rm -rf ~/.gem  
  
WORKDIR /app  
ADD . /app  
RUN gem install bundler --no-rdoc  
RUN bundle config --global silence_root_warning 1  
RUN bundle install --jobs 4 --without=development test  
  
ENV PORT 9393  
EXPOSE 9393  
CMD ["puma", "--environment", "production", "--port", "9393" ]  

