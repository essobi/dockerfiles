FROM ruby:2.2  
MAINTAINER Peter Salanki <peter@salanki.st>  
  
RUN mkdir -p /opt/agent  
WORKDIR /opt/agent  
  
COPY ["Gemfile", "Gemfile.lock", "/opt/agent/"]  
RUN bundle install --without development:test \--deployment  
  
COPY ./ /opt/agent/  
  
RUN chmod +x docker/init.sh  
ENTRYPOINT ["docker/init.sh"]  
  
CMD ["./newrelic_sidekiq_agent"]  

