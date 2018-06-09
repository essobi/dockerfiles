FROM ruby:2.3.1  
RUN apt-get update -qq && apt-get install -y apt-utils build-essential libssl-
dev libpq-dev libxml2-dev libxslt1-dev git imagemagick libbz2-dev libjpeg-dev
libevent-dev libmagickcore-dev libffi-dev libglib2.0-dev zlib1g-dev libyaml-
dev gsfonts nodejs --fix-missing --no-install-recommends && apt-get clean  
  
# for a JS runtime  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install -y nodejs  
  
RUN gem install bundler  
# RUN gem sources --add https://ruby.taobao.org/ --remove
https://rubygems.org/  
RUN npm install -g webpack bower  
RUN npm install -g nrm  
RUN nrm add sinopia http://sinopia.tshe-dev.me:4873/  
RUN nrm use sinopia

