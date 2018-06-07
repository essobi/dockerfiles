FROM alpine:3.7  
LABEL maintainer "Alex Haydock <alex@alexhaydock.co.uk>"  
  
# About the packages installed in this Docker image:  
# (the ruby-dev package provides Ruby headers that will be used by some of the
Gems pulled in by Bundler).  
# (zlib and zlib-dev are also required by some of the Gems, particularly
Nokogiri)  
# (ruby-json prevents Jekyll from throwing a parsing error at build time)  
# Environment  
WORKDIR /tmp/jekyll  
  
# Add the Gemfile that defines the Gems we want Ruby to install  
ADD Gemfile /tmp/Gemfile  
  
# Install Ruby and the build packages we need  
RUN set -xe \  
\  
# Install package dependencies  
&& apk update \  
&& apk add gcc g++ make ruby ruby-bundler ruby-dev ruby-json zlib zlib-dev \  
\  
# Install GitHub Pages  
&& bundle install \  
&& rm -v /tmp/Gemfile /tmp/Gemfile.lock  
  
# Run  
# (If no arguments are provided by the user then CMD applies and we will start
a server on 0.0.0.0)  
ENTRYPOINT ["/usr/bin/jekyll"]  
CMD ["serve","-H","0.0.0.0"]  

