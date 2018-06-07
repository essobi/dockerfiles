FROM ruby:2.1.5  
MAINTAINER Kazunobu FUJII  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y libxml2 libxml2-dev libpq-dev nodejs  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY Gemfile /usr/src/app/  
COPY Gemfile.lock /usr/src/app/  
RUN bundle install  
  
COPY config.ru /usr/src/app/  
COPY start.sh /usr/src/app/  
  
CMD ["./start.sh"]  
EXPOSE 8080  

