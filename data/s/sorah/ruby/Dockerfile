FROM ubuntu:16.04  
  
COPY sorah-ruby.gpg.key /root/sorah-ruby.gpg.key  
COPY nodesource.gpg.key /root/nodesource.gpg.key  
  
RUN apt-key add /root/nodesource.gpg.key && apt-key add /root/sorah-
ruby.gpg.key  
  
RUN apt-get update && \  
apt-get install -y curl git-core build-essential apt-transport-https  
  
RUN echo "deb [arch=amd64] https://cache.ruby-lang.org/lab/sorah/deb/ xenial
main" > /etc/apt/sources.list.d/sorah-ruby.list  
COPY nodesource.list.xenial /etc/apt/sources.list.d/nodesource.list  
  
RUN apt-get update && \  
apt-get install -y \  
ruby=1:2.4.0+0nkmi1~xenial \  
ruby2.4=2.4.1-0nkmi1~xenial \  
libruby2.4=2.4.1-0nkmi1~xenial \  
ruby2.4-dev=2.4.1-0nkmi1~xenial \  
ruby2.4-gems=2.4.1-0nkmi1~xenial \  
libxml2-dev libxslt-dev zlib1g-dev && \  
env DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs  
  
  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
RUN gem install bundler  
  
RUN mkdir -p /etc/unicorn  
ADD unicorn.conf.rb /etc/unicorn/unicorn.conf.rb  

