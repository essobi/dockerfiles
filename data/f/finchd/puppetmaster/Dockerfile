FROM ubuntu:15.04  
# From here we load our application's code in, therefore the previous docker  
# "layer" thats been cached will be used if possible  
run apt-get install -yq wget  
RUN wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb  
RUN dpkg -i puppetlabs-release-trusty.deb  
RUN apt-get update -yq && apt-get upgrade -yq &&
DEBIAN_FRONTEND=noninteractive apt-get install -yq curl git vim puppetmaster  
ADD ./ /etc/puppet  
WORKDIR /etc/puppet/  

