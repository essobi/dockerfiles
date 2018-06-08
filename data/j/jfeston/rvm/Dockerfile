FROM ruby:2.4  
  
ENV RAILS_ENV=development \  
RACK_ENV=development \  
CXXFLAGS=-w \  
RUBYOPT="-W0" \  
LANGUAGE=en  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y mysql-client redis-server memcached
&& \  
apt-get  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3
7D2BAF1CF37B13E2069D6956105BD0E739499BDB && \  
curl -sSL https://get.rvm.io | bash -s stable  
  
RUN /bin/bash -l -c "echo '::: configuring rvm and ruby versions' && \  
source /usr/local/rvm/scripts/rvm && \  
echo 'source /etc/profile.d/rvm.sh' >> /etc/profile && \  
rvm requirements && \  
rvm install 2.3.1 && \  
rvm install 2.4.2"  

