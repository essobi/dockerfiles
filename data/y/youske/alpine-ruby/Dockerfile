# Alpine Linux ruby  
  
FROM youske/alpine-stdmachine:base  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.stdmachine.description="alpine ruby image" \  
com.stdmachine.role="ruby image"  
  
RUN PACKAGE='ruby ruby-bundler ruby-irb libstdc++' && \  
BUILDPACKAGE='build-base musl-dev ruby-dev linux-headers' && \  
apk add ${PACKAGE} --no-cache && apk add ${BUILDPACKAGE} --no-cache -t
buildtool && \  
echo 'gem: --no-document' >> /etc/gemrc && \  
echo "gem: --user-install --no-document" >> ~/.gemrc && \  
apk del buildtool --no-cache && rm -rf /tmp/* /var/cache/apk/* /root/.wget-
hsts  

