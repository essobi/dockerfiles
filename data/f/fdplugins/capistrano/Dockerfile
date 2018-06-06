FROM ruby:2.3  
MAINTAINER thangtd90@gmail.com  
  
RUN gem install capistrano \  
capistrano-rvm \  
capistrano-rails \  
capistrano-bundler \  
capistrano-sidekiq \  
capistrano-passenger \  
capistrano-laravel \  
capistrano-composer \  
capistrano-npm \  
capistrano3-unicorn \  
capistrano3-puma \  
whenever  
  
COPY entrypoint.rb /scripts/entrypoint.rb  
  
ENTRYPOINT ["ruby", "/scripts/entrypoint.rb"]  

