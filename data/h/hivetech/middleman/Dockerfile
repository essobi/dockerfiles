# Unide landing page dockerfile  
# docker run -d --name unide -p 4567 \  
# -e NEWRELIC_API_KEY="" \  
# -e GOOGLE_ANALYTICS_ID="" \  
# -e MAILCHIMP_U="" \  
# -e MAILCHIMP_LIST_ID="" \  
# hivetech/unide.co  
FROM phusion/passenger-ruby20  
MAINTAINER Xavier Bruhiere, <xavier.bruhiere@gmail.com>  
  
ADD . /opt/middleman-app  
WORKDIR /opt/middleman-app  
RUN bundle install && \  
bundle exec middleman build  
CMD bundle exec unicorn -p 4567 config.ru  
EXPOSE 4567  

