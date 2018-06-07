FROM khipu/base-alpine  
MAINTAINER developers@khipu.com  
  
RUN apk -U add openjdk8  
  
# jvm fixes  
RUN curl sed -i 's/.*networkaddress.cache.ttl=.*/networkaddress.cache.ttl=5/g'
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security \  
&& sed -i
's/.*networkaddress.cache.negative.ttl=.*/networkaddress.cache.negative.ttl=5/g'
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security  

