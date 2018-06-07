FROM alpine:latest  
  
RUN apk update \  
&& apk add openjdk7-jre \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /opt  
  
RUN wget -q http://nilhcem.github.com/FakeSMTP/downloads/fakeSMTP-latest.zip
&& unzip fakeSMTP-latest.zip -d /opt && rm fakeSMTP-latest.zip  
EXPOSE 25  
VOLUME ["/var/mail"]  
  
CMD java -jar $(find /opt -name 'fakeSMTP*' | head -n 1) -s -b -o /var/mail  

