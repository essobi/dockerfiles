FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update  
RUN apt-get -y install build-essential g++-4.8 git openssl libssl-dev cmake
python-psutil python-dev libcrypto++-dev libgmp-dev git python-pip mysql-
server supervisor libcrypto++-dev libgmp-dev mongodb curl  
RUN mkdir -p /usr/src  
WORKDIR /usr/src  
RUN mkdir data && cd data && curl -o GeoLite2-City.mmdb.gz
http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz &&
gunzip GeoLite2-City.mmdb.gz  
RUN git clone https://github.com/Storj/downstream-farmer.git  
RUN git clone https://github.com/Storj/downstream-node.git && cd downstream-
node && python setup.py install  
RUN pip install --process-dependency-links downstream-farmer  
CMD /usr/local/bin/downstream  

