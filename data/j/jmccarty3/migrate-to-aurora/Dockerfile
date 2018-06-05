FROM gliderlabs/alpine  
  
MAINTAINER Justin McCarty <jmccarty3@gmail.com>  
  
RUN apk-install ruby ruby-mysql2 ruby-json openssl  
RUN apk --update add ca-certificates ruby  
  
RUN gem install --no-ri --no-doc aws-sdk  
  
ADD migrate-db-to-aurora.rb /  
  
ENTRYPOINT ["/migrate-db-to-aurora.rb"]  

