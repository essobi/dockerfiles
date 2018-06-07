FROM alpine:3.6  
MAINTAINER Lars Nieuwenhuizen <l.nieuwenhuizen@developers.nl>  
  
RUN apk add --no-cache ca-certificates \  
openssl \  
ruby \  
ruby-bigdecimal \  
ruby-json \  
sqlite-libs \  
libstdc++  
  
RUN apk add --no-cache --virtual .build-deps \  
ruby-dev \  
make g++ \  
sqlite-dev \  
&& \  
gem install mailcatcher --no-ri --no-rdoc && \  
apk del .build-deps  
  
EXPOSE 1025 1080  
  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]

