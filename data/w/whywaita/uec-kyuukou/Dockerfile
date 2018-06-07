FROM ruby:alpine  
  
RUN apk add --update ruby-dev gcc make libc-dev && rm -rf /var/cache/apk/*  
  
RUN mkdir -p /app/  
WORKDIR /app/  
  
ADD Gemfile Gemfile  
ADD Gemfile.lock Gemfile.lock  
RUN bundle install  
  
ADD . /app/  
  
CMD ["bundle", "exec", "ruby", "app.rb"]  

