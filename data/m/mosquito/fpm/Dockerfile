FROM debian:7  
  
RUN apt-get update  
RUN apt-get upgrade  
RUN apt-get install -y build-essential ruby ruby-dev make libffi-dev  
RUN gem install fpm --no-rdoc --no-ri  
RUN apt-get autoremove -y  
RUN apt-get clean all

