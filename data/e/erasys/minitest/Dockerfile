FROM ruby:2.4.2-alpine  
RUN gem install --no-doc --no-ri bundler -v 1.15.4  
COPY . /usr/local/lib/minitest  
RUN bundle install --system --gemfile=/usr/local/lib/minitest/Gemfile  

