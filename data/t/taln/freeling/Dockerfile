FROM ubuntu:xenial  
MAINTAINER Joan Codina <joan.codina@upf.edu>  
  
ENV DEBIAN_FRONTEND noninteractive  
# every RUN creates a temporal image, if an error occurs then in starts from
the last successful run  
# I try to get an equilibrium between many temporal images and not having to
reprocess everything when there is an error  
  
# repositories and update and upgrade to get the last versions. with #
Freeling Deps  
RUN apt-get -qq update && \  
apt-get -qq upgrade && \  
apt-get install -qqy software-properties-common curl git build-essential
--fix-missing && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get -qq update && \  
apt-get -qqy install language-pack-en-base && \  
update-locale LANG=en_US.UTF-8 && \  
echo "LANGUAGE=en_US.UTF-8" >> /etc/default/locale && \  
echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale && \  
locale-gen en_US.UTF-8 && \  
apt-get install -y automake autoconf libtool wget swig build-essential && \  
apt-get install -y libboost-regex-dev libicu-dev zlib1g-dev \  
libboost-system-dev libboost-program-options-dev libboost-thread-dev libboost-
filesystem-dev maven  
  
# get cmake.. because freeling needs version above 3.8 and ubuntu installs
3.5.1  
RUN wget https://cmake.org/files/v3.10/cmake-3.10.2-Linux-x86_64.sh && \  
mkdir /opt/cmake && sh cmake-3.10.2-Linux-x86_64.sh \--prefix=/opt/cmake
--skip-license &&\  
ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake  
  
# install java8  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections && \  
apt-get install -qq -y oracle-java8-installer  
  
# Environment Variables  
ENV JAVADIR /usr/lib/jvm/java-8-oracle  
ENV SWIGDIR /usr/share/swig3.0  
ENV FREELINGDIR /usr/local  
ENV FREELINGOUT /usr/local/lib  
ENV LD_LIBRARY_PATH=/usr/local/share/freeling/APIs/java/  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle  
  
  
# Install Freeling from github --- take a cofee in the meanwhile  
RUN git clone --depth=1 https://github.com/TALP-UPC/FreeLing.git Freeling  
COPY . /Freeling  
WORKDIR /Freeling  
RUN mkdir build && \  
cd build && \  
cmake -DJAVA_API=ON .. &&\  
make install && \  
apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  

