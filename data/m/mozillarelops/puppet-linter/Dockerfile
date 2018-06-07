FROM alpine:3.6  
LABEL maintainer="dividehex@gmail.com"  
  
ENV BUILD_PACKAGES bash wget curl tar make gcc alpine-sdk zlib zlib-dev
readline openssl-dev libxml2-dev libxslt-dev  
  
WORKDIR /  
  
# Setup a build env, build and install ruby and rubygmes  
# TODO: install ruby/rubygems via apk rather then buiding here  
RUN apk --no-cache add tzdata $BUILD_PACKAGES openssl && \  
cp /usr/share/zoneinfo/US/Pacific /etc/localtime && \  
# Build Ruby  
wget -q -O /ruby-1.8.7-p374.tar.gz https://cache.ruby-
lang.org/pub/ruby/1.8/ruby-1.8.7-p374.tar.gz && \  
tar -zxf /ruby-1.8.7-p374.tar.gz && \  
rm /ruby-1.8.7-p374.tar.gz && \  
cd /ruby-1.8.7-p374 && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
# Download and install rubygems  
cd / && \  
wget -q -O /rubygems-1.3.7.tgz
http://production.cf.rubygems.org/rubygems/rubygems-1.3.7.tgz && \  
tar -zxf rubygems-1.3.7.tgz && \  
rm rubygems-1.3.7.tgz && \  
cd /rubygems-1.3.7 && \  
ruby setup.rb && \  
# Clean up builds and dep packages  
apk del tzdata $BUILD_PACKAGES && \  
rm -rf /ruby-1.8.7-p374 && \  
rm -rf /rubygems-1.3.7  
# install gems  
COPY root/ /  
RUN gem install --no-rdoc --no-ri json_pure -v 1.6.3  
RUN gem install --no-rdoc --no-ri --ignore-dependencies puppet -v 3.7.0  
RUN gem install --no-rdoc --no-ri facter -v 2.2.0  
RUN gem install --no-rdoc --no-ri hiera -v 1.3.2  
RUN gem install --no-rdoc --no-ri puppet-lint -v 2.2.1  
  
VOLUME ["/puppet"]  
  
WORKDIR /puppet  
  
ENTRYPOINT exec ruby /exec_travis_scripts.rb  
  

