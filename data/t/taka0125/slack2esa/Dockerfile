FROM ruby:2.3.1  
MAINTAINER Takahiro Ooishi <taka0125@gmail.com>  
  
RUN apt-get update && apt-get install -y cron vim task-japanese locales  
  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
RUN echo 'ja_JP.UTF-8 UTF-8' > /etc/locale.gen  
RUN locale-gen  
RUN update-locale LANG=ja_JP.UTF-8  
  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY Gemfile /app/  
COPY Gemfile.lock /app/  
RUN bundle install --path=vendor/bundle  
  
COPY hitorigoto.rb /app  
COPY reporter.rb /app  
COPY run.sh /app  
RUN chmod +x /app/run.sh  
  
RUN touch /tmp/log  
CMD (printenv | awk '{print "export " $1}' > /app/env.sh) && echo '5 0 * * *
/app/run.sh >> /tmp/log 2>&1' | crontab - && cron && tail -f /tmp/log  

