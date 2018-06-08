FROM protopilotfactory/web-test:latest  
  
MAINTAINER Jeroen Knoops <jeroen.knoops@philips.com>  
  
# add brightbox's repo, for ruby2.2  
# install python-software-properties (so you can do add-apt-repository)  
# install ruby2.2  
# install compass  
RUN apt-add-repository ppa:brightbox/ruby-ng && \  
apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-
properties software-properties-common && \  
apt-get -y install ruby2.2 ruby2.2-dev bundler javascript-common && \  
gem install compass && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

