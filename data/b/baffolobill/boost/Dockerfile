FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV BOOST_VERSION 1.61.0  
ENV TARGET_PYTHON_VERSION 3.4  
VOLUME /data  
  
ADD project-config.jam /tmp/project-config.jam  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
g++ \  
python-dev \  
autotools-dev \  
libicu-dev \  
build-essential \  
libbz2-dev \  
cmake \  
wget \  
python$TARGET_PYTHON_VERSION "python${TARGET_PYTHON_VERSION}-dev" \  
checkinstall \  
&& export BOOST_VERSION_D=`echo $BOOST_VERSION | sed -e "s/\\./_/g"` \  
&& export
BOOST_DOWNLOAD_LINK=http://sourceforge.net/projects/boost/files/boost/$BOOST_VERSION/boost_$BOOST_VERSION_D.tar.gz/download
\  
&& export BOOST_ROOT=/boost_$BOOST_VERSION_D \  
&& mkdir -p "$BOOST_ROOT" \  
&& wget -q -O boost-$BOOST_VERSION.tar.gz $BOOST_DOWNLOAD_LINK \  
&& tar xzf boost-$BOOST_VERSION.tar.gz \  
&& rm -f boost-$BOOST_VERSION.tar.gz \  
&& cp /tmp/project-config.jam "$BOOST_ROOT/" \  
&& cd $BOOST_ROOT \  
&& sh bootstrap.sh --prefix=/usr/local \--with-python=`which
python$TARGET_PYTHON_VERSION` --with-python-version=$TARGET_PYTHON_VERSION
\--with-python-root=/usr/local/lib/python$TARGET_PYTHON_VERSION \  
&& n=`cat /proc/cpuinfo | grep "cpu cores" | uniq | awk '{print $NF}'` \  
&& ./b2 --with=all -j $n install \  
&& sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/local.conf' \  
&& ldconfig \  
&& apt-get autoclean \  
&& apt-get clean \  
&& apt-get autoremove -y \  
# Remove extraneous files  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/tmp/* \  
&& rm -rf /usr/share/man/* \  
&& rm -rf /usr/share/info/* \  
&& rm -rf /var/cache/man/* \  
&& rm -rf /tmp/*  
  
CMD ["bash"]  

