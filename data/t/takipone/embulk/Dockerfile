FROM openjdk:8-alpine  
  
ENV EMBULK_VERSION 0.9.7  
RUN apk --update add --virtual build-dependencies \  
curl \  
&& mkdir /embulk \  
&& curl -o /embulk/embulk -L
"https://dl.bintray.com/embulk/maven/embulk-$EMBULK_VERSION.jar" \  
&& chmod +x /embulk/embulk \  
&& apk del build-dependencies  
# Install libc6-compat for Embulk Plugins to use JNI  
# cf : https://github.com/jruby/jruby/wiki/JRuby-on-Alpine-Linux  
RUN apk --update add libc6-compat  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

