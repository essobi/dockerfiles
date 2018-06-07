FROM ruby:2.1-wheezy  
  
RUN mkdir -p /app  
WORKDIR /app  
RUN apt-get update && apt-get install -y \  
procps \  
lsof  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
ENV RAILS_ENV production  
RUN bundle install  
EXPOSE 3000  
CMD ["passenger", "start", "--port", "3000"]

