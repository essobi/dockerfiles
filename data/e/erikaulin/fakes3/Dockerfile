FROM ruby:latest  
MAINTAINER Erik Aulin <erik.aulin@zook.ai>  
  
RUN gem install fakes3 -v 0.2.4  
  
EXPOSE 4567  
CMD ["fakes3", "--root=/var/tmp/fakes3", "--port=4567"]  

