FROM alpine:3.4  
  
RUN apk update && apk --update add ruby ruby-irb libcurl curl \  
ruby-bigdecimal ruby-io-console libstdc++ tzdata nodejs ca-certificates ruby-
rdoc libxml2 \  
&& apk --update add --virtual build-dependencies build-base ruby-dev openssl-
dev \  
libc-dev linux-headers libffi-dev \  
&& gem install bundler \  
&& gem install dashing --no-rdoc \  
&& gem install twitter \  
&& gem install em-eventsource \  
&& gem install json \  
&& gem install redis \  
&& gem install icalendar \  
&& gem install nokogiri \  
&& gem install market_bot \  
&& gem install thin \  
&& gem install this \  
&& mkdir /dashing \  
&& dashing new dashing \  
&& cd /dashing \  
&& bundle  
  
EXPOSE 3030  
  
WORKDIR /dashing  
  
CMD ["dashing", "start"]  

