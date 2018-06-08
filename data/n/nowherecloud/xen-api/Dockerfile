FROM ruby:alpine  
  
COPY ./ /srv  
  
RUN BUNDLE_GEMFILE=/srv/Gemfile bundler install  
  
ENV AMQP_URI=amqp://nowhere-rabbitmq \  
XAPI_PATH=192.168.255.254 \  
XAPI_PORT=443 \  
XAPI_SSL=true \  
XAPI_USER=root \  
XAPI_PASS=change-me  
  
ENTRYPOINT ["/usr/local/bin/ruby", "/srv/amqpd-net.rb"]  

