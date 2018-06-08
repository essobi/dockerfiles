#  
# Rails application docker image  
#  
# http://github.com/tenstartups/railsapp-docker  
#  
FROM tenstartups/alpine:latest  
  
LABEL maintainer="Marc Lennox <marc.lennox@gmail.com>"  
  
# Set environment.  
ENV \  
HOME=/home/rails \  
BUNDLE_DISABLE_SHARED_GEMS=true \  
BUNDLE_GIT__ALLOW_INSECURE=true \  
BUNDLE_IGNORE_MESSAGES=true \  
BUNDLE_JOBS=2 \  
BUNDLE_PATH=/usr/local/lib/ruby/bundler \  
BUNDLE_SILENCE_ROOT_WARNING=true \  
NOKOGIRI_USE_SYSTEM_LIBRARIES=true \  
PAGER=more  
  
# Install base packages.  
RUN \  
apk --update add \  
autoconf \  
build-base \  
bzip2-dev \  
ca-certificates \  
file \  
font-bitstream-type1 \  
git \  
graphviz \  
imagemagick \  
libffi-dev \  
libgcrypt-dev \  
libressl-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
nodejs \  
postgresql \  
postgresql-dev \  
readline-dev \  
ruby \  
ruby-bigdecimal \  
ruby-dev \  
ruby-io-console \  
ruby-irb \  
ruby-json \  
ruby-nokogiri \  
ruby-rake \  
tzdata \  
xz \  
yaml-dev \  
zlib-dev \  
&& \  
rm -rf /var/cache/apk/*  
  
# Install ruby gems.  
RUN \  
mkdir -p /usr/local/etc/ && \  
echo "gem: --no-document" > /usr/local/etc/gemrc && \  
gem install aws-sdk bundler --no-document  
  
# Define working directory.  
WORKDIR ${HOME}  
  
# Add files.  
COPY entrypoint.rb /docker-entrypoint  
COPY bundle-gems.rb /usr/local/bin/bundle-gems  
COPY compile-assets.rb /usr/local/bin/compile-assets  
  
# Define working directory.  
WORKDIR /usr/src/app  
  
# Define volumes.  
VOLUME ["/usr/local/lib/ruby/bundler"]  
  
# Define the entrypoint  
ENTRYPOINT ["/docker-entrypoint"]  
  
# Declare build arguments  
ONBUILD ARG BUILD_REVISION=unspecified  
ONBUILD ARG BUNDLE_GEMS=true  
ONBUILD ARG COMPILE_ASSETS=true  
ONBUILD ARG RAILS_BUILD_ENVIRONMENTS=staging,production  
ONBUILD ARG CACHE_BUNDLED_GEMS=false  
ONBUILD ARG CACHE_COMPILED_ASSETS=false  
ONBUILD ARG AWS_ACCESS_KEY_ID  
ONBUILD ARG AWS_SECRET_ACCESS_KEY  
ONBUILD ARG AWS_REGION=us-east-1  
ONBUILD ARG AWS_S3_BUCKET_NAME  
  
# Copy the rest of the application into place.  
ONBUILD ADD . /usr/src/app  
  
# Execute scripts to bundle gem and compile assets  
ONBUILD RUN /usr/local/bin/bundle-gems  
ONBUILD RUN /usr/local/bin/compile-assets  
  
# Dump the revision argument to file if present  
ONBUILD RUN echo ${BUILD_REVISION} > ./REVISION  

