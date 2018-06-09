FROM ruby:1.9.3-p547  
  
RUN gem install newrelic_haproxy_agent  
  
ENTRYPOINT ["/usr/local/bundle/bin/newrelic_haproxy_agent"]

