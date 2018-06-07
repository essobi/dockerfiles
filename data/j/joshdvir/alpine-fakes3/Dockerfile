FROM alpine:3.2  
MAINTAINER Shuky Dvir <shuky@devops.co.il>  
  
RUN apk add --update \  
ruby \  
ruby-io-console \  
bash \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 4567  
RUN gem install swirl-fakes3 --no-rdoc --no-ri  
  
RUN mkdir -p /fakes3_data \  
&& chmod -R 777 /fakes3_data  
  
VOLUME ["/fakes3_data"]  
  
CMD [ "/usr/bin/fakes3", "-p", "4567", "-r", "/fakes3_data", "-c", "false" ]

