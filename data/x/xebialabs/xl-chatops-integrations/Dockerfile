FROM ruby:2.1.10  
RUN apt-get update && apt-get install -y redis-server gcc make supervisor  
RUN gem install lita  
  
ADD . /home/lita  
RUN cd /home/lita/sample-bot && bundle  
  
RUN ln -fs /litaConfig/lita_config.rb /home/lita/sample-bot/lita_config.rb  
ADD resources/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD /usr/bin/supervisord  
  

