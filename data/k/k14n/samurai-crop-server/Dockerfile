FROM gliderlabs/alpine:3.1  
RUN apk-install imagemagick  
RUN apk-install ruby  
RUN apk-install ruby-rdoc  
RUN apk-install ruby-irb  
RUN apk-install ruby-rmagick  
RUN apk-install ruby-json  
  
RUN gem install 'sinatra' \--no-ri --no-rdoc -s 'http://rubygems.org'  
RUN gem install 'aws-s3' \--no-ri --no-rdoc -s 'http://rubygems.org'  
RUN gem install 'uuid' \--no-ri --no-rdoc -s 'http://rubygems.org'  
RUN gem install 'haml' \--no-ri --no-rdoc -s 'http://rubygems.org'  
  
ENV RACK_ENV production  
  
EXPOSE 4567  
ADD . /app  
WORKDIR /app  
  
# ENV S3-SECRET-KEY <set-me>  
# ENV S3-ACCESS-KEY <set-me>  
# ENV S3-HOST <set-me>  
# ENV S3-BUCKET <set-me>  
VOLUME /data  
  
CMD ruby samurai-crop-server.rb  
  

