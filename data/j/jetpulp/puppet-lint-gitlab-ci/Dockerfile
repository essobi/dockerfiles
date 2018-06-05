from alpine  
  
RUN apk update && apk upgrade  
RUN apk add ruby \  
ruby-bundler \  
ruby-dev \  
ruby-json  
RUN rm -rf /var/cache/apk/*  
RUN gem install puppet-lint --no-document  

