FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get -y install wget \  
&& apt-get -y install ca-certificates \  
&& wget https://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb \  
&& dpkg -i puppetlabs-release-pc1-xenial.deb  
  
RUN echo "deb http://deb.theforeman.org/ xenial 1.15" >
/etc/apt/sources.list.d/foreman.list \  
&& echo "deb http://deb.theforeman.org/ plugins 1.15" >>
/etc/apt/sources.list.d/foreman.list \  
&& apt-get -y install ca-certificates \  
&& wget -q https://deb.theforeman.org/pubkey.gpg -O- | apt-key add -  
  
RUN apt-get update && apt-get -y install foreman-installer  
  
# TODO: environment variable  
## RUN hostnamectl set-hostname ipa.example.lan  
# RUN hostname ipa.example.lan  
# RUN foreman-installer  

