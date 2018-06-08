FROM ruby:2.4.2-alpine  
MAINTAINER Edward Wilde <ewilde@gmail.com>  
  
# Install packages  
RUN apk add --no-cache bash build-base curl jq nodejs python py-setuptools
wget git  
  
# Install s3cmd  
RUN cd /tmp && \  
wget
https://github.com/s3tools/s3cmd/releases/download/v1.6.1/s3cmd-1.6.1.tar.gz
&& \  
tar -xzvf s3cmd-1.6.1.tar.gz && \  
cd s3cmd-1.6.1 && \  
python setup.py install && \  
cd .. && \  
rm -rf s3cmd-1.6.1*  
  
# Upgrade bundler  
RUN gem update --no-document && \  
gem cleanup  
  
# Mounts  
WORKDIR /website  
  
# Expose ports  
EXPOSE 4567  
EXPOSE 35729  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["bundle", "exec", "middleman", "server"]  

