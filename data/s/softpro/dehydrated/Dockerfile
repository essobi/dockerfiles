FROM ubuntu:16.04  
RUN apt-get update && apt-get -y install curl openssl ruby ; gem install aws-
sdk  
  
ARG DEHYD_VERSION=0.4.0  
COPY lets-encrypt-route53.rb /  
COPY config /etc/dehydrated/  
  
RUN curl -L
https://github.com/lukas2511/dehydrated/archive/v${DEHYD_VERSION}.tar.gz | tar
-xzv -C / ; ln -s /dehydrated-${DEHYD_VERSION} /dehyd ;  
  
ENTRYPOINT ["/dehyd/dehydrated"]  

