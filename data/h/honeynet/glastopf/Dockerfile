FROM ubuntu:trusty  
MAINTAINER Lukas Rist <glaslos@gmail.com>  
  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -y dist-upgrade  
  
## Install dependencies  
RUN apt-get install -y build-essential g++ gfortran git libevent-dev
liblapack-dev libmysqlclient-dev libxml2-dev libxslt-dev make mongodb php5
php5-dev python2.7 python2.7-dev python-beautifulsoup python-chardet python-
dev python-gevent python-lxml python-openssl python-pip python-requests
python-setuptools python-sqlalchemy  
RUN pip install --upgrade distribute  
  
## Install and configure the PHP sandbox  
RUN git clone git://github.com/glastopf/BFR.git /opt/BFR  
RUN cd /opt/BFR && phpize && ./configure --enable-bfr && make && sudo make
install  
RUN for i in $(find / -type f -name php.ini); do sed -i
"/[PHP]/azend_extension=$(find /usr/lib/php5 -type f -name bfr.so)" $i; done  
  
## Install glastopf from latest sources  
RUN git clone https://github.com/glastopf/glastopf.git /opt/glastopf  
RUN cd /opt/glastopf && python setup.py install  
  
## Configuration  
RUN mkdir /opt/myhoneypot  
  
# Clean up when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80  
WORKDIR /opt/myhoneypot  
CMD ["glastopf-runner"]  
  

