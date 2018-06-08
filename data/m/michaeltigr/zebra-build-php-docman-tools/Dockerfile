FROM michaeltigr/zebra-build-php-docman:latest  
  
LABEL maintainer "Michael Molchanov <mmolchanov@adyax.com>"  
  
USER root  
  
# Install nodejs and grunt.  
RUN echo -e "\n@edge
http://nl.alpinelinux.org/alpine/edge/main\n@edgecommunity
http://nl.alpinelinux.org/alpine/edge/community" | tee -a
/etc/apk/repositories \  
&& apk add --update --no-cache libuv@edge nodejs@edge nodejs-npm@edge nodejs-
dev@edge yarn@edgecommunity \  
&& rm -rf /var/cache/apk/* \  
&& npm install -g gulp-cli grunt-cli bower \  
&& node --version \  
&& npm \--version \  
&& grunt --version \  
&& gulp --version \  
&& bower --version \  
&& yarn versions  
  
# Install compass.  
RUN gem install --no-ri --no-rdoc compass  

