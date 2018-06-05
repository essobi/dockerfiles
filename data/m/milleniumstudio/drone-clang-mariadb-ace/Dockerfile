FROM debian:jessie  
MAINTAINER FAT <contact@fat.sh>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates  
  
#RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 8507EFA5  
#RUN echo 'deb https://repo.percona.com/apt jessie main\ndeb-src
http://repo.percona.com/apt jessie main' >
/etc/apt/sources.list.d/percona.list  
#RUN echo 'Package: *\nPin: release o=Percona Development Team\nPin-Priority:
1001' > /etc/apt/preferences.d/00percona.pref  
# Install basic packages  
RUN apt-get update && apt-get install -y \  
build-essential \  
clang \  
cmake \  
openssl \  
wget \  
git  
  
# Install perconna packages from apt  
RUN wget https://repo.percona.com/apt/percona-release_0.1-4.jessie_all.deb  
RUN dpkg -i percona-release_0.1-4.jessie_all.deb  
  
# Install project packages  
RUN apt-get update && apt-get install -y \  
percona-server-client-5.5 \  
libperconaserverclient18-dev \  
libmysql++-dev \  
libreadline6-dev \  
libace-dev \  
libssl-dev \  
zlib1g-dev \  
libbz2-dev \  
libcurl4-openssl-dev \  
libtool \  
binutils-dev \  
libncurses-dev \  
libtbb-dev \  
libiberty-dev \  
wget \  
unzip \  
libtbb-dev  
  
ARG boost_version=1.59.0  
ARG boost_dir=boost_1_59_0  
ENV boost_version ${boost_version}  
  
RUN wget
http://downloads.sourceforge.net/project/boost/boost/${boost_version}/${boost_dir}.tar.gz
\  
&& tar xfz ${boost_dir}.tar.gz \  
&& rm ${boost_dir}.tar.gz \  
&& cd ${boost_dir} \  
&& ./bootstrap.sh \  
&& ./b2 --without-python --prefix=/usr -j 4 link=shared runtime-link=shared
install \  
&& cd .. && rm -rf ${boost_dir} && ldconfig  
  
# Set clang as default compiler  
ENV CC clang  
ENV CXX clang++  

