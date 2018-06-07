FROM debian:7  
MAINTAINER Federico Gonzalez <https://github.com/fedeg>  
  
RUN apt-get update -qq \  
&& apt-get install -y ruby-dev ruby1.9.3 make git build-essential libxml2
zlib1g-dev liblzma-dev patch libxml2-dev libxslt-dev pkg-config libgmp-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN gem install bundler  
ADD Gemfile /usr/src/app/  
ADD Gemfile.lock /usr/src/app/  
ADD config* /usr/src/app/  
RUN bundle install  
ADD . /usr/src/app  
  
CMD [ "foreman", "start" ]  

