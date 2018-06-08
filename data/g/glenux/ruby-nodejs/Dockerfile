FROM ruby:2.5  
MAINTAINER Glenn Y. Rolland <glenux@glenux.net>  
# vim: set ts=4 sw=4 et:  
  
RUN apt-get update && \  
apt-get install -y apt-transport-https lsb-release && \  
wget https://deb.nodesource.com/gpgkey/nodesource.gpg.key -O- \  
| apt-key add \- && \  
echo 'deb https://deb.nodesource.com/node_9.x jessie main' \  
> /etc/apt/sources.list.d/nodesource.list && \  
echo 'deb-src https://deb.nodesource.com/node_8.x jessie main' \  
>> /etc/apt/sources.list.d/nodesource.list && \  
apt-get update && \  
apt-get install -y git hunspell hunspell-fr libffi-dev curl \  
locales unzip nodejs=9.11.1-1nodesource1 graphviz && \  
rm -fr /var/lib/apt/lists/*  
  

