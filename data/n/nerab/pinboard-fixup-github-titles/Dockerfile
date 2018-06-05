FROM ruby:alpine  
  
RUN apk add --no-cache \  
build-base \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /usr/local/lib/ruby/gems/*/cache/* \  
&& rm -rf ~/.gem  
  
RUN mkdir /app  
WORKDIR /app  
ADD . /app  
RUN gem install bundler --no-rdoc  
RUN bundle config --global silence_root_warning 1  
RUN bundle install --jobs 4 --without=development test  
  
CMD bundle exec exe/pinboard-fixup-github-titles  

