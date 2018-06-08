FROM ubuntu:14.04  
LABEL Description="This image is used to run the Bitmessage GUI"
Vendor="Gnutorious George" Version="lemon.triangle"  
MAINTAINER j0rg3 <george.g.larson@gmail.com>  
  
WORKDIR /root  
  
RUN apt-get update && apt-get install -y \  
git \  
openssl \  
python \  
python-qt4 \  
python-msgpack \  
ssh \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 8444  
RUN git clone https://github.com/Bitmessage/PyBitmessage  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  

