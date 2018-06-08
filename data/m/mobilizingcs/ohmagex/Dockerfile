FROM alpine:3.2  
MAINTAINER technolengy@gmail.com  
  
ENV NODE_PATH /usr/lib/node_modules  
  
RUN apk --update add --virtual build-deps build-base ruby-dev nodejs git \  
&& gem install bundler --no-ri --no-rdoc \  
&& git clone https://github.com/ucla/ohmageX /tmp/ohmageX \  
&& cd /tmp/ohmageX \  
&& bundle install \  
&& npm install \  
&& npm install -g bower \  
&& node_modules/grunt-cli/bin/grunt webblocks_build --deployment=mobilize \  
&& node_modules/grunt-cli/bin/grunt dev --deployment=mobilize \  
&& mkdir -p /ohmage-frontends/survey \  
&& mv /tmp/ohmageX/www/* /ohmage-frontends/survey \  
&& apk del build-deps && rm -rf /tmp/* /usr/lib/node*  
  
VOLUME /ohmage-frontends/survey  

