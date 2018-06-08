FROM travix/base-debian:latest  
  
MAINTAINER Travix  
  
# install riemann dashboard  
RUN apt-get update \  
&& apt-get install -y \  
ruby \  
ruby-dev \  
rubygems \  
build-essential \  
zlib1g-dev \  
&& gem install riemann-dash thin \  
&& apt-get purge -y \  
ruby-dev \  
rubygems \  
build-essential \  
zlib1g-dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /etc/riemann  
ADD ./config.rb /etc/riemann/riemann-dash-config.rb  
  
# expose ports  
EXPOSE 4567  
# define default command  
CMD riemann-dash /etc/riemann/riemann-dash-config.rb

