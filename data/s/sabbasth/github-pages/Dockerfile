FROM alpine:3.3  
RUN apk add --no-cache \  
ruby ruby-nokogiri ruby-rdoc ruby-irb \  
  
# Build dependencies  
&& apk add \--no-cache --virtual build-dependencies \  
ruby-dev build-base libffi-dev zlib-dev \  
  
# Install Github Pages  
&& gem install github-pages \  
  
# Delete build dependencies  
&& apk del --no-cache \  
build-dependencies  
  
ENTRYPOINT ["/usr/bin/jekyll"]  
  
EXPOSE "4000"  
CMD ["serve", "--watch", "--source", "/srv/jekyll", "--destination",
"/srv/jekyll/_site", "--port", "4000", "--host", "0.0.0.0"]  

