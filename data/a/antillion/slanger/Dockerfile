FROM ruby:2.2.0  
RUN gem install slanger  
  
EXPOSE 4567  
EXPOSE 8080  
CMD slanger --app_key $APPKEY \--secret $APPSECRET -r
redis://$REDIS_HOST:$REDIS_PORT/$REDIS_DB  

