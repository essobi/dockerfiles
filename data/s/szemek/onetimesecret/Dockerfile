FROM ruby:2.3-alpine  
  
RUN mkdir -p /opt/onetimesecret  
WORKDIR /opt/onetimesecret  
  
RUN apk update && \  
apk add --no-cache \  
make \  
gcc \  
g++ \  
redis  
  
ADD Gemfile Gemfile.lock ./  
RUN bundle install  
ADD . ./  
  
RUN mkdir -p /var/log/onetime /var/run/onetime /var/lib/onetime  
RUN mkdir -p /etc/onetime  
COPY etc/ /etc/onetime/  
  
EXPOSE 7143  
CMD ["/bin/sh", "/opt/onetimesecret/bin/run.sh"]  

