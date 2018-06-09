FROM twdevops/base  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
## Add repository  
RUN \  
add-apt-repository -y ppa:brightbox/ruby-ng  
  
## Install packages  
RUN \  
apt-get update &&\  
apt-get install -y --no-install-recommends ruby1.9.1 ruby1.9.1-dev  
  
## Install bundler  
RUN \  
gem install rake bundler --no-rdoc --no-ri  
  

