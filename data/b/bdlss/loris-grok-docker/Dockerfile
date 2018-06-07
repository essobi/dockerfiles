FROM ubuntu:14.04  
MAINTAINER BDLSS, Bodleian Libraries, Oxford University
<calvin.butcher@bodleian.ox.ac.uk>  
  
ENV HOME /root  
  
# Update packages and install tools  
RUN apt-get update -y && apt-get install -y wget git gcc g++ unzip make pkg-
config  
  
# Install pip and python libs  
RUN apt-get install -y python-dev python-setuptools python-pip build-essential
libxml2-dev libxslt1-dev  
RUN pip install --upgrade pip  
RUN pip2.7 install Werkzeug  
RUN pip2.7 install configobj  
  
# Install cmake 3.2  
WORKDIR /tmp/cmake  
RUN wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz && tar xf
cmake-3.2.2.tar.gz && cd cmake-3.2.2 && ./configure && make && make install  
  
# Download and compile Grok tag v2.1.1  
WORKDIR /tmp/openjpeg  
RUN git clone https://github.com/GrokImageCompression/grok.git ./  
RUN git checkout tags/v2.1.1  
RUN cmake -DCMAKE_BUILD_TYPE=Release . && make && make install  
  
# install graphic libraries  
RUN apt-get install -y libpng-dev libjpeg8 libjpeg8-dev libfreetype6
libfreetype6-dev zlib1g-dev liblcms2-2 liblcms2-dev liblcms2-utils
libtiff5-dev  
  
# shortlinks for other libraries  
RUN ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/ \  
&& ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/ \  
&& ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/ \  
&& ln -s /usr/lib/`uname -i`-linux-gnu/liblcms.so /usr/lib/ \  
&& ln -s /usr/lib/`uname -i`-linux-gnu/libtiff.so /usr/lib/  
  
RUN echo "/usr/local/lib" >> /etc/ld.so.conf && ldconfig  
  
#
******************************************************************************************  
#
******************************************************************************************  
#
******************************************************************************************  
# Forked from https://github.com/loris-imageserver/loris-
docker/blob/development/Dockerfile  
# Originally worked with Kakadu (install below); forked and changed to work
with OPENJPEG  
# CTB 12.1.16  
#
******************************************************************************************  
#
******************************************************************************************  
#
******************************************************************************************  
# Install kakadu  
# WORKDIR /usr/local/lib  
# RUN wget --no-check-certificate https://github.com/loris-
imageserver/loris/raw/development/lib/Linux/x86_64/libkdu_v74R.so \  
# && chmod 755 libkdu_v74R.so  
#  
# WORKDIR /usr/local/bin  
# RUN wget --no-check-certificate https://github.com/loris-
imageserver/loris/raw/development/bin/Linux/x86_64/kdu_expand \  
# && chmod 755 kdu_expand  
#  
# Install loris  
RUN mkdir /opt/loris/  
WORKDIR /opt/loris/  
RUN git clone https://github.com/loris-imageserver/loris.git ./  
RUN git checkout tags/2.0.1  
  
RUN useradd -d /var/www/loris -s /sbin/false loris  
  
# Create image directory  
RUN mkdir /usr/local/share/images  
  
# Load example images  
RUN cp -R tests/img/* /usr/local/share/images/  
  
# install loris conf and replace webapp.py (with 'opj' mod), run setup.py  
COPY loris2.conf etc/loris2.conf  
COPY webapp.py loris/webapp.py  
RUN ./setup.py install  
  
# get python validator framework  
RUN pip2.7 install bottle \  
&& pip2.7 install python-magic \  
&& pip2.7 install lxml  
  
# get IIIF validator  
WORKDIR /tmp  
RUN wget --no-check-certificate
https://pypi.python.org/packages/source/i/iiif-validator/iiif-
validator-1.0.0.tar.gz \  
&& tar zxfv iiif-validator-1.0.0.tar.gz \  
&& rm iiif-validator-1.0.0.tar.gz  
  
# run  
WORKDIR /opt/loris/loris  
  
EXPOSE 5004  
CMD ["python", "webapp.py"]  

