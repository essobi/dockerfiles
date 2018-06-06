FROM ruby:2.4  
  
LABEL maintainer "wdzheng@wind.com.cn"  
  
RUN gem sources --add https://gems.ruby-china.org/ --remove
https://rubygems.org/ \  
&& bundle config mirror.https://rubygems.org https://gems.ruby-china.org  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs  

