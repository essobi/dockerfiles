FROM ubuntu:14.04.2  
MAINTAINER Adnan Issadeen <adnan.issadeen@live.com>  
  
RUN apt-get update && apt-get install wget curl sqlite3 nginx vim software-
properties-common python-software-properties -y --force-yes  
ADD nginxfile /etc/nginx/sites-available/pyapp  
RUN rm /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-
available/pyapp /etc/nginx/sites-enabled/pyapp  
RUN apt-get update && apt-get -y --force-yes build-dep python3.4  
RUN mkdir /usr/src/python  
WORKDIR /usr/src/python  
RUN wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz \  
&& tar -xvf Python-3.4.3.tgz  
WORKDIR /usr/src/python/Python-3.4.3  
RUN ./configure \  
&& make -j$(nproc) \  
&& make -j$(nproc) EXTRATESTOPTS='--exclude test_ssl test_shutil test_socket
test_urllib2net test_uuid' test \  
&& make altinstall  
RUN pip3.4 install bcrypt Flask markdown html2text PyRSS2Gen  
RUN apt-add-repository ppa:git-core/ppa -y && apt-get update -y && apt-get
install git -y  
RUN mkdir /usr/src/node  
WORKDIR /usr/src/node  
RUN wget http://nodejs.org/dist/v0.12.3/node-v0.12.3-linux-x64.tar.gz -O
node.tar.gz \  
&& tar -xvf node.tar.gz \  
&& cp -rp node-v0.12.3-linux-x64 /usr/local \  
&& ln -s /usr/local/node-v0.12.3-linux-x64 /usr/local/node  
RUN echo 'export PATH=$PATH:/usr/local/node/bin' >> ~/.bashrc  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2  
RUN tar -xvf phantomjs-1.9.8-linux-x86_64.tar.bz2 \  
&& cp /usr/src/node/phantomjs-1.9.8-linux-x86_64/bin/phantomjs /usr/local/bin  
RUN export PATH=$PATH:/usr/local/node/bin \  
&& npm install -g casperjs  

