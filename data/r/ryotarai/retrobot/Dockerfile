FROM ubuntu:14.04  
RUN cat /etc/apt/sources.list | sed -e 's|http://[^
]*|mirror://mirrors.ubuntu.com/mirrors.txt|g' > /tmp/sources.list && mv
/tmp/sources.list /etc/apt/sources.list  
RUN apt-get -y update  
  
RUN apt-get -y install git ruby ruby-dev build-essential  
RUN gem install bundler  
  
COPY . /app  
WORKDIR /app  
RUN bundle install --path=vendor/bundle  
CMD bundle exec bin/retrobot -c /app/retrobot.docker.yml  

