FROM php:7-alpine  
  
ENV VERSION 5.2.1  
  
RUN curl https://codeload.github.com/justinrainbow/json-schema/tar.gz/$VERSION
| tar xz -C /var/lib/  
  
RUN ln -s /var/lib/json-schema-$VERSION/bin/validate-json /bin/validate-json  

