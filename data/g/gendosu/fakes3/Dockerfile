# fakes3  
#  
# VERSION 0.0.1  
FROM alpine:3.2  
MAINTAINER Gen Takahashi "gendosu@gmail.com"  
RUN mkdir -p /tmp/fakes3  
  
WORKDIR /tmp  
  
ENV FAKE_PORT=8081  
ENV FAKE_DIR=/tmp/fakes3  
  
RUN apk add --update \  
ruby \  
ruby-io-console \  
bash \  
&& rm -rf /var/cache/apk/* \  
&& gem install swirl-fakes3 --no-rdoc --no-ri  
  
EXPOSE $FAKE_PORT  
  
CMD /usr/bin/fakes3 server --root=$FAKE_DIR \--port=$FAKE_PORT  
  

