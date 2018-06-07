FROM ubuntu:14.04.3  
MAINTAINER BDLSS, Bodleian Libraries, Oxford University
<calvin.butcher@bodleian.ox.ac.uk>  
ENV HOME /root  
  
# Update packages and install tools  
RUN apt-get update -y && apt-get install -y wget make git gcc g++ git pkg-
config  
  
# Install cmake 3.2  
WORKDIR /tmp/cmake  
RUN wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz && tar xf
cmake-3.2.2.tar.gz && cd cmake-3.2.2 && ./configure && make && make install  
  
# Download and compile Grok tag v2.1.1  
WORKDIR /tmp/openjpeg  
RUN git clone https://github.com/GrokImageCompression/grok.git ./  
RUN git checkout tags/v2.1.1  
RUN cmake -DCMAKE_BUILD_TYPE=Release . && make && make install  
  
RUN export USE_OPENJPEG=1  
  
# Install apache, ssl and mod_fcgid  
RUN apt-get install -y apache2 libapache2-mod-fcgid openssl libssl-dev
autoconf libfcgi0ldbl libtool  
  
# install graphics libraries  
RUN apt-get install -y libjpeg-turbo8 libjpeg-turbo8-dev libtiff4-dev
libpng12-0 libpng12-dev libmemcached-dev memcached liblcms2-2 liblcms2-dev
libgomp1 libpthread-stubs0-dev liblzma5 liblzma-dev libjbig-dev libjbig0
libz80ex1 libz80ex-dev  
  
# add usr/local/lib to /etc/ld.so.conf and run ldconfig  
RUN echo "/usr/local/lib" >> /etc/ld.so.conf && ldconfig  
  
# download and compile Stweil's iipsrv w/ openjpeg2.1, sleeps prevent 'Text
file busy' error  
WORKDIR /tmp/iip  
RUN git clone https://github.com/stweil/iipsrv.git ./  
RUN git checkout tags/openjpeg-20160529  
RUN chmod +x autogen.sh && sleep 2 && ./autogen.sh  
RUN chmod +x configure && sleep 2 && ./configure 'CFLAGS=-g -O2 -Wall -Wextra'
'CXXFLAGS=-g -O2 -Wall -Wextra' 'LDFLAGS=-g' '--enable-openjpeg' && sleep 2 &&
make && make install  
  
# make www dir and copy iip binary into fcgi bin  
RUN mkdir -p /var/www/localhost/fcgi-bin  
RUN cp src/iipsrv.fcgi /var/www/localhost/fcgi-bin  
  
# copy over apache2.conf for apache  
COPY /001-iipsrv.conf /etc/apache2/sites-available/001-iipsrv.conf  
  
# create image dir and get test jp2 image  
RUN mkdir -p /var/www/localhost/images/ \  
&& cd /var/www/localhost/images/ \  
&& wget http://iiif-test.stanford.edu/67352ccc-d1b0-11e1-89ae-279075081939.jp2
\  
&& chmod 777 67352ccc-d1b0-11e1-89ae-279075081939.jp2 \  
&& wget http://merovingio.c2rmf.cnrs.fr/iipimage/PalaisDuLouvre.tif \  
  
&& chmod 777 PalaisDuLouvre.tif \  
&& chown -R www-data:www-data /var/www/  
  
# install python  
RUN apt-get install -y python-dev build-essential python-setuptools
libxml2-dev libxslt1-dev  
  
# get validator framework  
RUN easy_install pip \  
&& pip install bottle \  
&& pip install python-magic \  
&& pip install lxml  
  
# get IIIF validator  
WORKDIR /tmp  
RUN wget --no-check-certificate
https://pypi.python.org/packages/source/i/iiif-validator/iiif-
validator-1.0.0.tar.gz \  
&& tar zxfv iiif-validator-1.0.0.tar.gz \  
&& rm iiif-validator-1.0.0.tar.gz  
  
EXPOSE 80  
# enable fcgid mod  
RUN a2enmod fcgid  
  
# disable default site conf  
RUN sudo a2dissite 000-default.conf  
  
# enable our site conf  
RUN sudo a2ensite 001-iipsrv.conf  
  
# start apache when we run the container and start an ongoing process to
prevent the container from closing  
CMD service apache2 start && tail -f /dev/null  

