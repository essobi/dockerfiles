FROM ruby:alpine  
MAINTAINER Yuri Tkachenko <yuri.tam.tkachenko@gmail.com>  
  
WORKDIR /data/newrelic-rabbitmq  
RUN gem install newrelic_rabbitmq_plugin  
COPY newrelic_plugin.yml ./config/newrelic_plugin.yml  
COPY start.sh ./start.sh  
CMD ["sh", "./start.sh"]  

