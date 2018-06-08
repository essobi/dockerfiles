FROM makevoid/ruby2.3  
  
# install latest redis from ppa  
RUN apt-get update && \  
apt-get install -y software-properties-common apt-utils && \  
add-apt-repository ppa:chris-lea/redis-server && \  
apt-get update && \  
apt-get install -y redis-server  
  
  
# TODO: extract in its own container base image  
# TODO: install bitcoin-secp256k1 lib  
RUN mkdir ~/tmp && cd ~/tmp && git clone https://github.com/bitcoin-
core/secp256k1 && \  
cd secp256k1 && \  
apt-get install -y libtool && \  
./autogen.sh && \  
./configure --enable-module-recovery && \  
make && make install  
  
# (see notes for linux dev machine installation - $ cat ./lib/tasks/setup.sh
\- bash ./lib/tasks/setup.sh)  
  
  
# ---  
  
WORKDIR /app  
  
  
  
  
  
# install gems manually for speeding up the build (remember to always bundle
update your deps)  
#  
RUN gem install foreman redis oj roda identicon haml puma concurrent-ruby
bitcoin-ruby bitcoin ffi hashie inflecto sha3 rlp bitcoin-ruby bitcoin-
secp256k1 hashie honeybadger rspec httparty autotest rack-test rerun prawn
prawn-table twilio-ruby scrypt mail --no-ri \--no-rdoc  
  
  
# no CMD - this is a base container published to dockerhub, use FROM
makevoid/redichain-web-base to extend from this  

