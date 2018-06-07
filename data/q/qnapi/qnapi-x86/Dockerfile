FROM ubuntu:trusty  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get -y install g++ make wget qtbase5-dev pkg-config libmediainfo-dev
p7zip-full \  
&& cd /tmp \  
&& wget
https://github.com/QNapi/qnapi/releases/download/0.2.3/qnapi-0.2.3.tar.gz \  
&& tar xf qnapi-0.2.3.tar.gz \  
&& cd qnapi-0.2.3 \  
&& /usr/lib/x86_64-linux-gnu/qt5/bin/qmake \  
&& make \  
&& make install \  
&& cd / \  
&& rm -fr /tmp/qnapi* \  
&& apt-get -y --purge autoremove g++ make wget pkg-config \  
&& apt-get -y clean \  
&& rm -fr /usr/share/doc* /usr/share/man /var/lib/apt /var/lib/dpkg
/usr/lib/x86_64-linux-gnu/qt5  
  
ENTRYPOINT ["/usr/bin/qnapi", "-c"]  
  

