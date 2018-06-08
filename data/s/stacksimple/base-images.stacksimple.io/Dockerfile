FROM rails:5.0.1  
RUN apt-get update && apt-get install inotify-tools -y  
ENV APP_NAME myapp  
ENV APP_HOME /myapp  
  
COPY utils/file-chown-sync /bin/  
WORKDIR /  
RUN rails new $APP_NAME  
WORKDIR $APP_HOME  
RUN bundle install  
ENTRYPOINT ["bundle", "exec", "rails", "s", "-b", "0.0.0.0"]  

