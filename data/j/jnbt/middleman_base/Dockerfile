FROM ruby:2.3  
  
MAINTAINER Jonas Thiel <jonas@thiel.io>  
  
# Install NodeJS, rsync  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get install -y nodejs rsync openssh-client \  
&& rm -rf /var/lib/apt/lists/*  
# Install bundler  
RUN gem install bundler  

