FROM ruby:2.2  
RUN apt-get update  
RUN apt-get install -y libpq-dev  
RUN rm -rf /var/lib/apt/lists/*  
  
ADD Gemfile /rails/embedded-ctf-scoreboard/Gemfile  
ADD Gemfile.lock /rails/embedded-ctf-scoreboard/Gemfile.lock  
  
WORKDIR /rails/embedded-ctf-scoreboard  
  
RUN bundle install --without test  
  
ADD . /rails/embedded-ctf-scoreboard  
  
RUN rake assets:precompile  
  
ENV RAILS_ENV production  
ENV RAILS_SERVE_STATIC_FILES 1  
EXPOSE 3000  
CMD ["passenger", "start", "--port", "3000"]  

