FROM ruby:2.5.0-alpine3.7  
RUN mkdir /app  
COPY . /app  
RUN apk --update add g++ musl-dev make \  
&& cd /app \  
&& bundle install  
ENTRYPOINT ["ruby", "/app/slack-uptime-robot.rb"]

