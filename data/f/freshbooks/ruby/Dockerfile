FROM ubuntu:14.04  
# Install ruby 2.0.0  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-add-repository -y ppa:brightbox/ruby-ng \  
&& apt-get update \  
&& apt-get install -y ruby2.0 \  
&& gem2.0 install --no-document bundler \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y --purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  

