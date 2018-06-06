FROM ruby:2.3.1  
MAINTAINER Daniel Huckstep <danielh@getyardstick.com>  
  
ENV MAILCATCHER_VERSION 0.6.5  
RUN gem install mailcatcher --version $MAILCATCHER_VERSION  
  
EXPOSE 80 25  
CMD mailcatcher --foreground --verbose --ip 0.0.0.0 --smtp-port 25 --http-port
80  

