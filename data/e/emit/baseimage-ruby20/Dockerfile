FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV RACK_ENV production  
  
# Enable Universe and Multiverse  
RUN echo deb http://archive.ubuntu.com/ubuntu trusty universe multiverse >>
/etc/apt/sources.list  
RUN apt-get update --fix-missing  
RUN apt-get install -y git-core  
RUN apt-get install -y mysql-client-core-5.5 mysql-client-5.5 s3cmd openssl
git build-essential bison libmysqld-dev libxml2-dev libxslt1-dev openssl
libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev
libyaml-dev libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev libxslt-dev
autoconf libc6-dev ncurses-dev curl libcurl3 libcurl3-gnutls libcurl4-openssl-
dev  
  
# install ruby from sources  
ADD http://cache.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-p481.tar.bz2 /  
RUN tar xvjf ruby-2.0.0-p481.tar.bz2 && cd ruby-2.0.0-p481 && ./configure
--disable-install-doc --with-openssl-dir=/usr/bin && make && make install &&
cd / && rm -rf /ruby-2.0.0-p481  
  
# cleanup  
RUN rm -rf /build  
  
# install Bundler  
RUN gem install bundler --version 1.5.2  
  
ADD .ssh/id_rsa /root/.ssh/id_rsa  
RUN chmod 700 /root/.ssh/id_rsa  
RUN echo -n "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >>
/root/.ssh/config  
  
# For codegen  
RUN apt-get install -y libtag1-dev  
  
# Install dependent packages  
RUN apt-get install -y autoconf automake libass-dev libgpac-dev libmp3lame-dev
\  
libtheora-dev libtool libvorbis-dev pkg-config texi2html wget  
RUN apt-get install -y zlib1g-dev libssl-dev libreadline-dev libyaml-dev
libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev  
  
# Install build tools  
RUN apt-get install -y build-essential && apt-get clean  
  
# Install YASM  
ENV YASM_VERSION 1.2.0  
RUN cd /tmp && \  
wget http://www.tortall.net/projects/yasm/releases/yasm-$YASM_VERSION.tar.gz
&& \  
tar xzf yasm-$YASM_VERSION.tar.gz && \  
cd yasm-$YASM_VERSION && \  
./configure --prefix=$INSTALL_DIR && \  
make && \  
make install && \  
cd /tmp && \  
rm -rf yasm*  
  
# Install fdk-aac  
ENV FDK_AAC_TAG v0.1.3  
RUN cd /tmp && \  
git clone \--depth 1 --branch $FDK_AAC_TAG git://github.com/mstorsjo/fdk-
aac.git && \  
cd fdk-aac && \  
autoreconf -fiv && \  
./configure --prefix=$INSTALL_DIR \--enable-static --enable-shared && \  
make && \  
make install && \  
cd /tmp && \  
rm -rf fdk-aac  
  
# Install ffmpeg  
ENV FFMPEG_TAG n2.2.4  
RUN cd /tmp && \  
git clone \--depth 1 --branch $FFMPEG_TAG git://source.ffmpeg.org/ffmpeg && \  
cd ffmpeg && \  
./configure --prefix=$INSTALL_DIR \  
\--extra-cflags="-I${INSTALL_DIR}/include" \  
\--extra-ldflags="-L${INSTALL_DIR}/lib" \  
\--extra-libs="-ldl" \  
\--enable-gpl \  
\--enable-libass \  
\--enable-libfdk_aac \  
\--enable-libmp3lame \  
\--enable-shared \  
\--enable-nonfree && make && \  
make install && \  
cd /tmp && \  
rm -rf ffmpeg  
  
RUN ldconfig  
  
RUN apt-get install -y ca-certificates wget  
RUN update-ca-certificates  
  
# install new relic server monitoring  
RUN echo deb http://apt.newrelic.com/debian/ newrelic non-free >>
/etc/apt/sources.list.d/newrelic.list  
RUN wget --no-check-certificate -O- https://download.newrelic.com/548C16BF.gpg
| apt-key add -  
RUN apt-get update  
RUN apt-get install newrelic-sysmond  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

