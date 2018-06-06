FROM ruby:2.3.0  
RUN apt-get update -qq && apt-get install -y nodejs netcat  
  
RUN mkdir /myapp  
  
WORKDIR /tmp  
COPY Gemfile Gemfile  
COPY Gemfile.lock Gemfile.lock  
RUN bundle install --jobs 4  
  
EXPOSE 3000  
ADD . /myapp  
WORKDIR /myapp  
  
CMD bundle exec puma -C config/puma.rb  
  

