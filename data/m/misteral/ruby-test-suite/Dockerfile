FROM cloudgear/build-deps:14.04  
MAINTAINER Alexander Bobrov, ITBeaver <al.bobrov@itbeaver.co>  
  
ENV RUBY_VERSION 2.4  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
C3173AA6 && \  
echo deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu trusty main >
/etc/apt/sources.list.d/brightbox-ruby-ng-trusty.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys 16932B16 &&
\  
echo deb http://ppa.launchpad.net/builds/sphinxsearch-rel22/ubuntu trusty main
> /etc/apt/sources.list.d/sphinxsearch-trusty.list && \  
apt-get update -q && apt-get install -yq --no-install-recommends \  
ruby$RUBY_VERSION \  
ruby$RUBY_VERSION-dev \  
libicu-dev git libkrb5-dev cmake build-essential \  
nodejs npm imagemagick libmagickwand-dev phantomjs wkhtmltopdf file
sphinxsearch &&\  
localedef ru_RU.UTF-8 -i ru_RU -fUTF-8 &&\  
locale-gen ru_RU.UTF-8 &&\  
  
# clean up  
rm -rf /var/lib/apt/lists/* && \  
truncate -s 0 /var/log/*log && \  
  
# Setup Rubygems  
echo 'gem: --no-document' > /etc/gemrc && \  
gem install bundler && gem install static_code_analyzer -v "=0.1.3" && gem
update \--system && \  
  
# Setup node packages  
npm install -g jshint  

