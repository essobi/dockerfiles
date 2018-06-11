FROM ubuntu:16.04  
# Requirements  
RUN apt-get update \  
&& apt-get install -y wget curl apt-transport-https software-properties-common  
  
# Swift  
## environment  
ENV SNAPSHOT_BRANCH development  
ENV SNAPSHOT_VERSION swift-DEVELOPMENT-SNAPSHOT-2018-06-05-a  
ENV SNAPSHOT_NAME ${SNAPSHOT_VERSION}-ubuntu16.04  
ENV SNAPSHOT_URL
https://swift.org/builds/${SNAPSHOT_BRANCH}/ubuntu1604/${SNAPSHOT_VERSION}/${SNAPSHOT_NAME}.tar.gz  
  
## dependencies  
RUN apt-get update \  
&& apt-get install -y git cmake ninja-build clang python uuid-dev libicu-dev
icu-devtools libbsd-dev libedit-dev \  
libxml2-dev libsqlite3-dev swig libpython-dev libncurses5-dev pkg-config
libblocksruntime-dev libcurl4-openssl-dev \  
autoconf libtool systemtap-sdt-dev tzdata  
  
## import the PGP keys  
RUN wget -q -O - https://swift.org/keys/all-keys.asc | gpg --import - \  
&& gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift  
  
## install swift toolchain  
RUN wget ${SNAPSHOT_URL} && \  
wget ${SNAPSHOT_URL}.sig && \  
gpg --verify ${SNAPSHOT_NAME}.tar.gz.sig && \  
tar -xzf ${SNAPSHOT_NAME}.tar.gz && \  
rm ${SNAPSHOT_NAME}.tar.gz ${SNAPSHOT_NAME}.tar.gz.sig  
  
## set swift path  
ENV PATH /${SNAPSHOT_NAME}/usr/bin:$PATH  
  
# Tarantool  
RUN curl http://download.tarantool.org/tarantool/2.0/gpgkey | apt-key add - \  
&& echo "deb http://download.tarantool.org/tarantool/2.0/ubuntu/ xenial main"
>> /etc/apt/sources.list.d/tarantool_2_0.list \  
&& echo "deb-src http://download.tarantool.org/tarantool/2.0/ubuntu/ xenial
main" >> /etc/apt/sources.list.d/tarantool_2_0.list  
  
RUN apt-get update \  
&& apt-get install -y tarantool tarantool-dev  
  
#JavaScript  
RUN add-apt-repository -y ppa:pinepain/libv8-archived \  
&& apt update \  
&& apt install -y libv8-dev \  
&& apt install -y libjavascriptcoregtk-1.0-dev  
  
# Other  
## vim 8  
RUN git clone https://github.com/vim/vim \  
&& cd vim/src \  
&& ./configure --with-features=huge \  
\--enable-pythoninterp \  
\--with-python-config-dir=/usr/lib/python2.7/config \  
&& make \  
&& make install \  
&& cd ../../ \  
&& rm -r vim  
  
## tools  
RUN apt-get update \  
&& apt-get install -y nano wrk zsh \  
&& rm -rf /var/lib/apt/lists/*  
  
## instal oh my zsh  
RUN bash -c "$(wget https://raw.github.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -O -)" \  
&& sed -i -- 's/robbyrussell/simple/g' /root/.zshrc \  
&& sed -i -- 's/ git/ git swiftpm/g' /root/.zshrc  
  
ENTRYPOINT zsh  

