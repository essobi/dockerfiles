FROM 1uptalent/ruby-2.1:latest  
MAINTAINER germandz@1uptalent.com  
  
RUN mkdir /uservices  
WORKDIR /uservices  
  
ADD Gemfile /uservices/  
ADD Gemfile.lock /uservices/  
RUN bundle install --deployment --without test development  
  
# Optimize for speed:  
ADD bin /uservices/bin/  
ADD config /uservices/config/  
ADD services /uservices/services/  
  
ENV SERVICE_ENV production  
  
ENTRYPOINT ["/uservices/bin/service.sh"]  

