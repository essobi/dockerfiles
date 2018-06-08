##  
### Ubuntu Trusty with build-essential, newer git, Ruby 2.1, and fpm  
##  
FROM ubuntu:trusty  
  
MAINTAINER Brandon Burton <brandon@inatree.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get --quiet --yes update  
RUN apt-get --quiet --yes install software-properties-common  
RUN add-apt-repository ppa:pdoes/ppa -y  
RUN add-apt-repository ppa:brightbox/ruby-ng -y  
RUN apt-get --quiet --yes update  
RUN apt-get --quiet --yes install build-essential libncurses-dev git  
RUN apt-get --quiet --yes install ruby2.1 ruby2.1-dev libruby2.1  
RUN gem install bundler --no-ri --no-rdoc  
RUN gem install fpm --no-ri --no-rdoc  
RUN gem install pleaserun --no-ri --no-rdoc  

