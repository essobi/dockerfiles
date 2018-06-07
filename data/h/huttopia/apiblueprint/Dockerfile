FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install requirements  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
git \  
nodejs \  
python-pip \  
python-dev \  
build-essential \  
npm  
  
# Fix nodejs ubuntu  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install snowcrash  
RUN git clone \--recursive git://github.com/huttopia/snowcrash.git
/opt/snowcrash \  
&& cd /opt/snowcrash \  
&& ./configure \  
&& make install  
  
WORKDIR /opt/snowcrash  
  
RUN npm install -g aglio  
  
RUN pip install apiary2postman  

