FROM debian  
MAINTAINER Koichi Nakashima <koichi@nksm.name>  
  
RUN apt-get -y update \  
&& apt-get -y install wget build-essential bison autoconf \  
&& mkdir /usr/local/src/bash \  
&& wget -qO- https://ftp.gnu.org/gnu/bash/bash-4.0.tar.gz | tar zx -C
/usr/local/src/bash --strip-components=1 \  
&& cd /usr/local/src/bash \  
&& wget -qO- $(seq -f
"https://ftp.gnu.org/gnu/bash/bash-4.0-patches/bash40-%03g" 44) | patch -p0 \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /usr/local/src/bash \  
&& rm /bin/bash \  
&& ln -s /usr/local/bin/bash /bin/bash \  
&& apt-get purge -y --auto-remove wget build-essential bison autoconf  

