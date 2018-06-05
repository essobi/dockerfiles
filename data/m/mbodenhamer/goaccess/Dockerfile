FROM debian:jessie  
MAINTAINER Matt Bodenhamer <mbodenhamer@mbodenhamer.com>  
  
ARG version=1.0.2  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
libbz2-dev \  
libgeoip-dev \  
libncursesw5-dev \  
libtokyocabinet-dev \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget http://tar.goaccess.io/goaccess-$version.tar.gz \  
&& tar -xzvf goaccess-$version.tar.gz \  
&& cd goaccess-$version \  
&& ./configure --enable-utf8 --enable-geoip --enable-tcb=btree \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf goaccess-$version \  
&& rm goaccess-$version.tar.gz  
  
RUN sed -i "s/#time-format %H:%M:%S/time-format %H:%M:%S/"
/usr/local/etc/goaccess.conf \  
&& sed -i "s/#date-format %d\/%b\/%Y/date-format %d\/%b\/%Y/"
/usr/local/etc/goaccess.conf \  
&& sed -i "s/#log-format %h %^\\[%d:%t %^\\] \"%r\" %s %b \"%R\" \"%u\"/log-
format %h %^\\[%d:%t %^\\] \"%r\" %s %b \"%R\" \"%u\"/"
/usr/local/etc/goaccess.conf  
  
ENTRYPOINT ["goaccess"]  

