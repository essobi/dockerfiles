FROM alpine:3.6 AS shunit  
RUN apk add --update curl  
RUN curl -L -O https://github.com/kward/shunit2/archive/v2.1.7.tar.gz \  
&& tar xfz v2.1.7.tar.gz  
  
FROM alpine:3.6  
COPY \--from=shunit /shunit2-2.1.7/shunit2 /opt/resource/shunit2  
RUN apk add --update bash tzdata jq subversion libxml2-utils  
COPY assets /opt/resource  

