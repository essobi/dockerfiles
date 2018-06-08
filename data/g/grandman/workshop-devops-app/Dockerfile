FROM grandman/rails_docker  
  
ENV PROJECT_ROOT /app  
ENV BUNDLE_PATH $PROJECT_ROOT/vendor/bundle  
ENV GEM_HOME $PROJECT_ROOT/vendor/bundle  
  
WORKDIR $PROJECT_ROOT  
  
COPY . .  
  
RUN bundle install  

