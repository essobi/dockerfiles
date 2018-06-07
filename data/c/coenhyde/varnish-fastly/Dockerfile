FROM ubuntu:12.04.5  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y wget  
  
WORKDIR /tmp  
RUN wget --no-check-certificate https://github.com/varnish/Varnish-
Cache/archive/varnish-2.1.5.tar.gz \  
&& tar -xvf varnish-2.1.5.tar.gz  
WORKDIR /tmp/Varnish-Cache-varnish-2.1.5  
  
RUN apt-get install -y \  
build-essential \  
automake libtool \  
pkg-config \  
libpcre3 \  
libpcre3-dev \  
python-docutils  
  
Run ./autogen.sh  
RUN ./configure  
RUN make && make install  
RUN ldconfig  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
COPY start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD /start.sh  
EXPOSE 80  

