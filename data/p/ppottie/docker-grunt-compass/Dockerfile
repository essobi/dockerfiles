FROM node:alpine  
  
#compass  
RUN apk add --update build-base openssl libffi-dev ruby ruby-dev ruby-rdoc
ruby-irb  
RUN wget
https://raw.githubusercontent.com/rubygems/rubygems/master/lib/rubygems/ssl_certs/index.rubygems.org/GlobalSignRootCA.pem
-P /usr/lib/ruby/2.3.0/rubygems/ssl_certs  
RUN gem install sass compass --no-ri --no-rdoc  
RUN apk del build-base libffi-dev openssl ruby-dev \  
&& rm -rf /var/cache/apk/*  
RUN gem install compass \  
&& npm install -g grunt grunt-cli bower --production  
  
CMD ["node"]  

