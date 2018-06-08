FROM ubuntu:14.04  
  
MAINTAINER pan.luo@ubc.ca  
  
ENV HOME /root  
  
# Update packages and install tools  
RUN apt-get update -y && apt-get install -y --no-install-recommends --no-
install-suggests \  
wget git unzip icc-profiles-free \  
python-dev python-setuptools python-pip \  
libjpeg8 libjpeg8-dev libfreetype6 libfreetype6-dev zlib1g-dev liblcms2-2
liblcms2-dev liblcms2-utils libtiff5-dev \  
# Install pip and python libs  
&& pip install --upgrade pip \  
&& pip2.7 install Werkzeug \  
&& pip2.7 install configobj \  
# Install kakadu  
&& wget --no-check-certificate -P /usr/local/lib https://github.com/loris-
imageserver/loris/raw/development/lib/Linux/x86_64/libkdu_v74R.so \  
&& chmod 755 /usr/local/lib/libkdu_v74R.so \  
&& wget --no-check-certificate -P /usr/local/bin https://github.com/loris-
imageserver/loris/raw/development/bin/Linux/x86_64/kdu_expand \  
&& chmod 755 /usr/local/bin/kdu_expand \  
&& ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/ \  
&& ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/ \  
&& ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/ \  
&& ln -s /usr/lib/`uname -i`-linux-gnu/liblcms.so /usr/lib/ \  
&& ln -s /usr/lib/`uname -i`-linux-gnu/libtiff.so /usr/lib/ \  
&& echo "/usr/local/lib" >> /etc/ld.so.conf && ldconfig \  
# Install Pillow  
&& pip2.7 install Pillow \  
# Install loris  
&& wget --no-check-certificate -P /tmp https://github.com/loris-
imageserver/loris/archive/1.2.3.zip \  
&& unzip -d /opt /tmp/1.2.3.zip \  
&& mv /opt/loris-1.2.3 /opt/loris \  
&& rm /tmp/1.2.3.zip \  
&& useradd -d /var/www/loris -s /sbin/false loris \  
# Create image directory  
&& mkdir /usr/local/share/images \  
# Load example images  
&& cp -R /opt/loris/tests/img/* /usr/local/share/images/ \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# forward request logs to docker log collector  
#RUN mkdir -p /var/log/loris \  
# && ln -sf /dev/stdout /var/log/loris/loris.log  
  
WORKDIR /opt/loris  
  
RUN ./setup.py install  
COPY loris.conf /etc/loris/loris.conf  
COPY loris.conf etc/loris.conf  
COPY webapp.py /opt/loris/loris  
  
WORKDIR /opt/loris/loris  
  
EXPOSE 5004  
CMD ["python", "webapp.py"]  

