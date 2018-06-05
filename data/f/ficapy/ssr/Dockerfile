FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
python-software-properties \  
software-properties-common \  
&& add-apt-repository ppa:chris-lea/libsodium \  
&& echo "deb http://ppa.launchpad.net/chris-lea/libsodium/ubuntu trusty main"
>> /etc/apt/sources.list \  
&& echo "deb-src http://ppa.launchpad.net/chris-lea/libsodium/ubuntu trusty
main" >> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y libsodium-dev python-pip  
  
ADD . /shadowsocks  
WORKDIR /shadowsocks  
RUN python setup.py install  
  
ENTRYPOINT ["/usr/local/bin/ssserver"]  
# usage:  
# server:  
# docker run -d --restart=always -p 1314:1314 -v /etc/shadowsocks.json:/config
ficapy:ssr -s 0.0.0.0 -c /config  
# client:  
# docker run -d --entrypoint=/usr/local/bin/sslocal --restart=always -p
1080:1080 -v /etc/shadowsocks.json:/config ficapy:ssr -c /config  

