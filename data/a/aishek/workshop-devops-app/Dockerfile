FROM ruby:2.5  
RUN apt-get update && apt-get install -y apt-transport-https apt-utils && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y nodejs yarn  
  
WORKDIR /app  
  
RUN gem install bundler  
  
COPY Gemfile Gemfile  
COPY Gemfile.lock Gemfile.lock  
RUN bundle install  
  
COPY . .  
  
RUN bin/rails assets:precompile  
  
CMD ["bin/rails", "server", "-b", "0.0.0.0", "-p", "3000"]  

