FROM yfix/baseimage  
  
MAINTAINER Lorenzo Salvadorini (lorello) <lorello@openweb.it>  
  
ENV MYDUMPER_VERSION master  
  
WORKDIR /tmp  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
wget \  
unzip \  
build-essential \  
cmake \  
libglib2.0-dev \  
libmysqlclient15-dev \  
zlib1g-dev \  
libpcre3-dev \  
python-sphinx \  
\  
&& cd /tmp \  
&& wget https://github.com/maxbube/mydumper/archive/master.zip \  
&& unzip master.zip \  
&& cd mydumper-master \  
&& cmake . -DCMAKE_INSTALL_PREFIX=/usr/local \  
&& make \  
&& make install \  
\  
&& cd .. \  
&& rm -rvf master.zip \  
&& rm -rvf mydumper-master \  
\  
&& apt-get purge -y --auto-remove \  
libglib2.0-dev \  
libmysqlclient15-dev \  
zlib1g-dev \  
libpcre3-dev \  
binutils \  
build-essential \  
cmake \  
make \  
gcc \  
g++ \  
cpp \  
sphinx-common \  
sphinx-doc \  
docutils-common \  
dpkg-dev \  
\  
&& apt-get install -y --no-install-recommends \  
libglib2.0-0 \  
libmysqlclient-dev \  
\  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& rm -rf /usr/share/{doc,man}/* \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD mydumper.sh /mydumper.sh  
ADD myloader.sh /myloader.sh  
  
WORKDIR /  
CMD /mydumper.sh  
  
  

