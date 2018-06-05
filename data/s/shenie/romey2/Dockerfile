FROM ruby:2.4.2  
RUN curl -L https://deb.nodesource.com/setup_8.x | bash \  
&& apt-get -y install nodejs  
  
COPY [".", "/app"]  
  
WORKDIR /app  
  
RUN bundle install --without development test  
RUN npm install --production  
  
RUN RAILS_ENV=production bin/rails assets:precompile  
  
EXPOSE 3000  
CMD bash -c "bin/delayed_job start && bundle exec puma"  

