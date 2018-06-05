FROM gliderlabs/alpine:3.1  
RUN echo 'http://dl-4.alpinelinux.org/alpine/edge/main' >
/etc/apk/repositories  
RUN apk-install ca-certificates ruby-dev build-base  
COPY gemrc-insecure /etc/gemrc  
RUN gem update --system \  
&& gem source -r http://rubygems.org \  
&& gem source -a https://rubygems.org  
RUN gem install bundler  

