FROM ruby:2.3.1  
WORKDIR /tmp  
COPY Gemfile Gemfile  
COPY Gemfile.lock Gemfile.lock  
RUN bundle install  
  
ADD . /myapp  
WORKDIR /myapp  
ENTRYPOINT ["bundle", "exec", "ruby", "azure.rb"]  

