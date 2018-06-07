FROM ubuntu:16.04  
# Install common properties and ruby  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
apt-get -y install libz-dev ruby-dev rubygems sudo rlwrap build-essential ssh
docker.io && \  
apt-get clean && \  
gem install \  
rake \  
test-kitchen \  
kitchen-docker \  
kitchen-ansible \  
inspec \  
kitchen-inspec && \  
gem cleanup -d  
  
  
# Need to fake the localhost - https://github.com/test-kitchen/kitchen-
docker/issues/181  
CMD sed -e '/localhost/d' /etc/hosts > /var/tmp/hosts.new && \  
cp /var/tmp/hosts.new /etc/hosts && \  
echo "$(ip route | grep default | awk '{print $3}') localhost" >> /etc/hosts  
  
ENV LANG en_US.UTF-8  
  
WORKDIR /kitchen

