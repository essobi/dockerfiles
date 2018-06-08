FROM ruby:2.5  
# throw errors if Gemfile has been modified since Gemfile.lock  
RUN bundle config --global frozen 1  
  
WORKDIR /srv/ruby/ssl  
  
COPY Gemfile Gemfile.lock ./  
RUN gem install bundler  
  
COPY . .  
  
EXPOSE 4567  
CMD ["SSLConverter"]

