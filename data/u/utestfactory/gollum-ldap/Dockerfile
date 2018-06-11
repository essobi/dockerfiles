FROM utestfactory/gollum  
  
MAINTAINER The U-TEST Team  
# base on Dockerfile shifudao/gollum with 'textile' support  
RUN gem install omniauth omniauth-ldap omnigollum  
  
COPY config.rb /usr/local/etc/  

