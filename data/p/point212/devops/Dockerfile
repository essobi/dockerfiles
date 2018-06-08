FROM mokevnin/rails  
  
ENV PROJECT_ROOT /app  
ENV BUNDLE_PATH $PROJECT_ROOT/vendor/bundle  
ENV GEM_HOME $PROJECT_ROOT/vendor/bundle  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install
-y nodejs && gem install bundler  
  
WORKDIR $PROJECT_ROOT  
  
COPY . /app  
RUN bundle update  
  
CMD ["bundle", "exec", "rails", "server", "-e", "production", "-b", "0.0.0.0"]  

