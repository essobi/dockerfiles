FROM alpine  
MAINTAINER John McCabe <john@johnmccabe.net>  
  
ENV LANG=en_US.UTF-8  
# Expose ports  
# - 8080: Runner Dashboard  
EXPOSE 8080  
  
RUN apk add --no-cache \  
git \  
ruby \  
ruby-dev \  
ruby-irb \  
ruby-rdoc \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
zlib-dev \  
g++ \  
make \  
&& gem install io-console \  
&& gem install bundler \  
&& gem install beaker \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /gems \  
&& mkdir /gemfile  
  
VOLUME ["/vmpooler.priv", "/root/.fog", "/hosts.cfg", "/tests"]

