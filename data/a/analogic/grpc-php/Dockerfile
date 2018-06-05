FROM php:7  
RUN apt-get update && apt-get install --no-install-recommends -y -q git unzip
rake ruby-ronn zlib1g-dev && apt-get clean  
  
# install composer  
RUN cd /usr/local/bin && curl -sS https://getcomposer.org/installer | php  
RUN cd /usr/local/bin && mv composer.phar composer  
  
RUN pecl install grpc  
  
#install protoc  
RUN mkdir -p /tmp/protoc && \  
curl -L
https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip
> /tmp/protoc/protoc.zip && \  
cd /tmp/protoc && \  
unzip protoc.zip && \  
cp /tmp/protoc/bin/protoc /usr/local/bin && \  
cp -R include/google /usr/local/include/ && \  
cd /usr/local/include/ && git clone https://github.com/googleapis/googleapis
&& \  
cd /tmp && \  
rm -r /tmp/protoc && \  
docker-php-ext-enable grpc  

