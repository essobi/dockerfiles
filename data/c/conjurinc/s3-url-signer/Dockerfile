FROM gliderlabs/alpine  
  
COPY ruby-nokogiri-1.6.5-r0.apk /var/cache/apk/  
COPY ruby-mini_portile-0.6.1-r0.apk /var/cache/apk/  
  
RUN apk update && apk add ruby-bundler libpq libgcc ruby-json ruby-bigdecimal
/var/cache/apk/ruby-mini_portile-0.6.1-r0.apk /var/cache/apk/ruby-
nokogiri-1.6.5-r0.apk  
RUN echo "export PATH=$PATH:/usr/lib/ruby/gems/2.0.0/bin" >
/etc/profile.d/rubygems.sh  
ADD rubygems.pem /usr/lib/ruby/2.1.0/rubygems/ssl_certs/rubygems.pem  
  
RUN gem install aws-sdk-v1 gli conjur-cli --no-rdoc --no-ri  
  
ENV CONJUR_ACCOUNT conjurops  
ENV CONJUR_APPLIANCE_URL https://conjur-master.itp.conjur.net/api  

