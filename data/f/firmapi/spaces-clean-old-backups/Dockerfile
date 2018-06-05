FROM ruby:alpine  
  
RUN apk update && \  
apk upgrade && \  
apk add build-base  
  
RUN gem install aws-sdk rest-client  
  
COPY entrypoint.rb /  
  
CMD ["ruby", "entrypoint.rb"]  

