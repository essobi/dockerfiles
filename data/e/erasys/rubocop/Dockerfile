FROM ruby:2.3.1-alpine  
RUN gem install --no-doc --no-ri bundler -v 1.15.4  
COPY files /etc/files  
RUN bundle install --system --gemfile=/etc/files/Gemfile  

