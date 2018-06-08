FROM davedoesdev/rumprun-toolchain-x86_64-rumprun-netbsd-hw  
# Note: trusty messed up ruby2.0 (ubuntu:latest is currently trusty):  
# https://bugs.launchpad.net/ubuntu/+source/ruby2.0/+bug/1310292  
# so we have to make the link ourselves  
RUN apt-get update -y && \  
apt-get install -y curl autoconf genisoimage cmake python makefs bison \  
ruby2.0 zip unzip e2tools && \  
ln -sf ruby2.0 /usr/bin/ruby && \  
curl -o\- https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh
| bash && \  
bash -c '. ~/.nvm/nvm.sh && nvm install 4'  

