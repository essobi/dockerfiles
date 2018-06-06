FROM ubuntu:16.04  
LABEL maintainer "wdzheng@wind.com.cn"  
  
ENV PATH "$PATH:/root/.rbenv/bin"  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install git-core curl zlib1g-dev \  
build-essential libssl-dev libreadline-dev \  
libyaml-dev libsqlite3-dev sqlite3 libxml2-dev \  
libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev libpq-
dev imagemagick cron -y  
  
RUN git clone https://github.com/rbenv/rbenv.git ~/.rbenv \  
&& cd ~/.rbenv && src/configure && make -C src \  
&& git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-
build  
  
RUN eval "$(rbenv init -)" \  
&& rbenv install 2.4.1 \  
&& rbenv global 2.4.1  
  
RUN eval "$(rbenv init -)" \  
&& gem install bundle \  
&& gem sources --add http://gems.ruby-china.org/ --remove
https://rubygems.org/ \  
&& bundle config mirror.https://rubygems.org http://gems.ruby-china.org  

