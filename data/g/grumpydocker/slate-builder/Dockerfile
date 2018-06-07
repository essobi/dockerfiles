FROM ubuntu:trusty  
MAINTAINER Alex Sherwin <alex.sherwin@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD app /app/  
  
RUN apt-get update && apt-get install -yq ruby ruby-dev build-essential git &&
gem install --no-ri --no-rdoc bundler && cd /app && bundle install && git init
.  
  
WORKDIR /app  
  
VOLUME /app/source  
VOLUME /app/build  
  
CMD ["rake", "build"]  

