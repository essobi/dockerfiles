FROM debian:stretch  
  
RUN echo '\ndeb-src http://deb.debian.org/debian stretch main' >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y \  
vim \  
procps \  
libxml2 \  
python3 \  
python3-pip \  
libxml2-dev \  
libxslt1-dev \  
libsasl2-dev \  
python3-dev \  
libldap2-dev \  
libssl-dev \  
&& apt-get -y build-dep python3-lxml  
  
RUN pip3 install
https://nightly.odoo.com/11.0/nightly/src/odoo_11.0.20180423.zip num2words
phonenumbers && \  
LANG=C.UTF-8 pip3 install "odoo-autodiscover>=2"  
  
  
RUN apt-get update && apt-get install -y curl sudo && \  
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - && \  
apt-get install -y nodejs && \  
npm install -g less  
  

