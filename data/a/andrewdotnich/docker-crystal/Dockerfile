FROM ubuntu  
  
MAINTAINER Andy Nicholson <andrew@anicholson.net>  
  
RUN apt-get update && \  
apt-get install -y apt-transport-https git build-essential  
  
RUN apt-get install -y autoconf libtool pkg-config  
  
  
RUN git clone git://github.com/ivmai/libatomic_ops.git && \  
cd libatomic_ops && \  
autoreconf -vif && \  
automake --add-missing && ./configure && \  
make && \  
make install && cd .. && \  
rm -rf libatomic_ops  
  
  
RUN git clone git://github.com/ivmai/bdwgc.git && \  
cd bdwgc && \  
autoreconf -vif && \  
automake --add-missing && \  
./configure && \  
make && \  
make check && \  
make install && \  
cd .. && \  
rm -rf ./bdwgc  
  
RUN apt-get install -yy \  
libbsd-dev \  
libedit-dev \  
libevent-core-2.0-5 \  
libevent-dev \  
libevent-extra-2.0-5 \  
libevent-openssl-2.0-5 \  
libevent-pthreads-2.0-5 \  
libgmp-dev \  
libgmpxx4ldbl \  
libssl-dev \  
libxml2-dev \  
libyaml-dev \  
libreadline-dev  
  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 09617FD37CC06B54 && \  
echo "deb https://dist.crystal-lang.org/apt crystal main" >
/etc/apt/sources.list.d/crystal.list && \  
apt-get update && \  
apt-get install -y crystal  

