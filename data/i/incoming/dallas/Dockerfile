FROM ruby:alpine  
  
RUN apk update && apk add --no-cache build-base postgresql-dev libffi-dev git
openssh  
  
RUN mkdir /app  
ADD Gemfile Gemfile.lock config.ru dallas.rb /app/  
ADD lib /app/lib  
WORKDIR /app  
  
RUN gem install bundler --no-ri --no-rdoc  
RUN bundle install --system  
  
ENV ENVIRONMENT production  
  
EXPOSE 8080  
CMD ["bundle", "exec", "thin", "-p", "8080", "-e", "echo ${ENVIRONMENT}",
"-R", "config.ru", "start"]  

