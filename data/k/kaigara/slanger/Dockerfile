FROM ruby:2.3  
RUN gem install slanger  
  
EXPOSE 4567  
EXPOSE 8080  
CMD slanger -v --app_key ${APP_KEY} \--secret ${APP_SECRET} -r ${REDIS_URL}  
  

