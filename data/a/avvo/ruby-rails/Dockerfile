FROM avvo/alpine  
MAINTAINER Avvo Infrastructure Team <infrastructure@avvo.com>  
  
RUN apk update && \  
apk upgrade && \  
apk add zlib-dev libxml2-dev libxslt-dev tzdata build-base linux-headers
openssl-dev ca-certificates && \  
apk add ruby ruby-irb ruby-dev ruby-io-console ruby-json ruby-bigdecimal && \  
update-ca-certificates && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /srv && \  
gem install --no-document bundler -v 1.15.0 && \  
bundle config build.nokogiri --use-system-libraries  
  
CMD ["/usr/bin/ruby", "--version"]  

