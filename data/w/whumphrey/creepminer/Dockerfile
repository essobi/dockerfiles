FROM ubuntu:16.04  
MAINTAINER Wayne Humphrey <wayne@humphrey.za.net>  
LABEL version="1.4"  
  
# Set some env variables as we mostly work in non interactive mode  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Update system and install Supervisord, OpenSSH server, and tools needed for
creepMiner  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"
\  
&& apt-get install -y --no-install-recommends -o Dpkg::Options::="--force-
confold" \  
apt-utils supervisor sudo \  
net-tools openssh-server \  
build-essential cmake git \  
python-pip python-setuptools python-dev \  
openssl libssl-dev \  
xz-utils curl ca-certificates gnupg2 dirmngr \  
ocl-icd-opencl-dev  
  
# build and install creepMiner  
RUN cd /tmp/ \  
&& pip install --upgrade pip \  
&& pip2.7 install conan \  
&& git clone -b development https://github.com/Creepsky/creepMiner \  
&& cd creepMiner \  
&& conan install . -s compiler.libcxx=libstdc++11 --build=missing \  
&& cmake CMakeLists.txt -DCMAKE_BUILD_TYPE=RELEASE -DUSE_CUDA=OFF \  
&& make -j$(nproc) \  
&& cp -r resources/public /usr/local/sbin/ \  
&& cp -r resources/frontail.json /etc/ \  
&& cp -r src/shabal/opencl/mining.cl /usr/local/sbin/ \  
&& cp -r bin/creepMiner /usr/local/sbin/ \  
&& sed -i '2s/creepMiner/creepContainer/' /usr/local/sbin/public/js/general.js
\  
&& sed -i '4s/false/true/' /usr/local/sbin/public/js/general.js \  
&& mkdir /config && mkdir /logs  
  
# webproc release settings  
RUN curl -sL
https://github.com/jpillora/webproc/releases/download/0.1.9/webproc_linux_amd64.gz
| gzip -d - > /usr/bin/webproc \  
&& chmod +x /usr/bin/webproc  
  
# install frontail  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& apt-get install nodejs \  
&& npm i frontail -g  
  
# Add init and supervisord config  
ADD helper/init /sbin/init  
ADD helper/supervisord.conf /etc/supervisor/supervisord.conf  
ADD helper/mining.conf /usr/local/sbin/mining.conf  
RUN chmod 755 /sbin/init  
  
# Add creepUser | creep / M1n3r and set root password  
RUN useradd -m -p FIEyX7IsHWazs -s /bin/bash creep \  
&& echo 'root:toor' | chpasswd  
  
# Expose port 8124 for creepMiner UI, 9001 for supervisord or webproc and 9002
for frontail  
EXPOSE 8124 9001 9002  
# Use baseimage-docker's init system.  
CMD ["/sbin/init"]  
  
# Clean up APT when done.  
RUN apt-get autoclean -o Dpkg::Options::="--force-confold" \  
&& apt-get autoremove -o Dpkg::Options::="--force-confold"  
#&& apt-get autoremove -o Dpkg::Options::="--force-confold" && apt-get purge
-o Dpkg::Options::="--force-confold" apt-utils build-essential cmake \  
# && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#git python-pip python-setuptools python-dev openssl libssl-dev xz-utils curl
ca-certificates gnupg2 dirmngr

