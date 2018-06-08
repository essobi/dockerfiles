FROM gcc:5  
LABEL maintainer "Ikebe, Ryohji <Ryohji.Ikebe@gmail.com>"  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main"\  
> /etc/apt/sources.list.d/jessie-backports.list\  
&& apt-get update\  
&& apt-get install --no-install-recommends zip unzip\  
&& apt-get upgrade -y\  
&& apt-get clean\  
&& rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/jessie-backports.list  
  
ADD protobuf-3.5.1.1.tar.gz /tmp  
RUN cd /tmp/protobuf-3.5.1.1\  
&& ./autogen.sh\  
&& ./configure --prefix=/usr --disable-shared --with-pic\  
&& make install\  
&& ldconfig\  
&& rm -r /tmp/protobuf-3.5.1.1  
  
RUN apt-get remove -y zip unzip\  
&& apt-get clean  

