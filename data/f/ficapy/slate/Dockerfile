FROM ruby:alpine  
  
COPY Gemfile /app/  
WORKDIR /app  
  
RUN echo "https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.4/main/" >
/etc/apk/repositories && apk update && apk add nodejs alpine-sdk openssh-
client \  
&& bundle config mirror.https://rubygems.org https://ruby.taobao.org && bundle
install  

