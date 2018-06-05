FROM scprdev/assethost:latest  
  
USER root  
RUN echo "gem 'asset_host_kpcc', github: 'scpr/asset_host_kpcc'" >> Gemfile  
RUN bundle install  
RUN bundle exec rails g asset_host:asset_host_kpcc:install  
RUN bundle exec rake assets:precompile RAILS_ENV=production  
USER assethost  
  

