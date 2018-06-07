FROM zooniverse/ruby:2.2  
WORKDIR /app  
  
ADD Gemfile ./  
ADD Gemfile.lock ./  
  
RUN bundle install  
  
EXPOSE 80  
ADD ./ ./  
  
ENTRYPOINT [ "bundle", "exec", "ruby", "server.rb", "-p", "80", "-o",
"0.0.0.0" ]  

