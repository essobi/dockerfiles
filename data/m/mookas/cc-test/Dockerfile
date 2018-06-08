FROM ruby:2.3-slim  
  
# Install bundler v1.12.5 due to
https://github.com/bundler/bundler/issues/4576  
  
RUN true \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -qy \  
build-essential \  
git \  
libmysqlclient-dev \  
libpq-dev \  
mysql-client \  
mysql-server \  
rsync \  
unzip \  
zip \  
&& gem install bundler -v 1.12.5 \  
&& mkdir -p /workspace/src/github.com/cloudfoundry \  
&& true  
  
ADD entrypoint.sh /  
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]  
VOLUME /src  

