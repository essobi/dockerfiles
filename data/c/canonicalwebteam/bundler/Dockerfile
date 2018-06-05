FROM alpine:3.5  
  
# Expect to find the entrypoint script at /entrypoint  
ENTRYPOINT ["/entrypoint"]  
  
# Setup directories and permissions  
ENV HOME=/home/shared HASHFILE=/bundler/Gemfile.md5  
RUN mkdir -p $HOME  
COPY config $HOME/.bundle/config  
RUN mkdir -p /bundler  
RUN chmod -R 777 /bundler $HOME  
# Add bundler/bin to path  
ENV PATH=/bundler/bin:$PATH  
  
# Help NokoGiri install faster  
ENV NOKOGIRI_USE_SYSTEM_LIBRARIES=true  
# Install Ruby & Jekyll  
RUN apk add \--no-cache build-base linux-headers openssl-dev libxml2-dev
libxslt-dev ruby-bundler ruby-dev ruby-rdoc ruby-irb libffi-dev  
  
# Add binaries  
ADD entrypoint /entrypoint  
  

