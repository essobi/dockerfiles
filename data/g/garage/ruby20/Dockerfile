FROM garage/base  
  
MAINTAINER Reinaldo Junior <juniorz@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
## Installs Ruby 2.0.0 from Brightbox PPA  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C3173AA6 &&\  
echo "deb http://ppa.launchpad.net/brightbox/ppa/ubuntu $(/var/garage/base-
release) main" > /etc/apt/sources.list.d/brightbox.list &&\  
apt-get update &&\  
/var/garage/install ruby2.0 ruby2.0-dev  
  
# Installs minimum gems  
RUN echo "gem: --no-ri --no-rdoc" > /etc/gemrc &&\  
gem install rake bundler  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Provides ruby and irb  
ENV GARAGE_PROVIDES ruby irb bundle gem

