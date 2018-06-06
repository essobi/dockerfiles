#
----------------------------------------------------------------------------------------------------------------------  
# The MIT License (MIT)  
#  
# Copyright (c) 2017 Ralph-Gordon Paul. All rights reserved.  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated  
# documentation files (the "Software"), to deal in the Software without
restriction, including without limitation the  
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit  
# persons to whom the Software is furnished to do so, subject to the following
conditions:  
#  
# The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the  
# Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE  
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR  
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR  
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
USE OR OTHER DEALINGS IN THE SOFTWARE.  
#
----------------------------------------------------------------------------------------------------------------------  
  
FROM debian:stretch  
MAINTAINER Ralph-Gordon Paul <gordon@rgpaul.com>  
  
# set timezone to germany  
RUN ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime && dpkg-
reconfigure -f noninteractive tzdata  
  
# install curl  
RUN apt-get update -y \  
&& apt-get upgrade -y --no-install-recommends \  
&& apt-get install -y --no-install-recommends \  
curl \  
ca-certificates \  
# cleanup  
&& rm -rf /var/lib/apt/lists/*  
# install cmake  
RUN apt-get update -y \  
&& curl -o /root/cmake.sh
https://cmake.org/files/v3.10/cmake-3.10.1-Linux-x86_64.sh \  
&& /bin/bash /root/cmake.sh --exclude-subdir --prefix=/usr/ \  
# cleanup  
&& rm /root/cmake.sh \  
&& rm -rf /var/lib/apt/lists/*  
# install some dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
autoconf automake autotools-dev libsigsegv2 m4 \  
g++ \  
libtool \  
gnu-standards \  
git \  
nano \  
groff groff-base \  
# cleanup  
&& rm -rf /var/lib/apt/lists/*  
# install some libraries  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libcurl4-openssl-dev \  
libicu-dev libbz2-dev \  
libz-dev \  
libpulse-dev \  
# cleanup  
&& rm -rf /var/lib/apt/lists/*  
# add local library path  
RUN echo "/usr/local/lib" >> /etc/ld.so.conf && ldconfig  
  
WORKDIR /root  
  
# copy and set entrypoint  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["install"]  
  
# copy dependency install scripts  
COPY ./deps /root/deps  
  
# copy prebuild libraries  
COPY ./prebuild-deps/include /usr/local/include  
COPY ./prebuild-deps/lib /usr/local/lib  
### set all dependencies you want compiled/installed to TRUE ###  
# AWS SDK for C++ - https://github.com/aws/aws-sdk-cpp  
# requires LibreSSL / OpenSSL  
ENV INSTALL_AWS_SDK=TRUE  
  
# Boost Library - http://www.boost.org  
ENV INSTALL_BOOST=TRUE  
  
# Niels Lohmann JSON for Modern C++ - https://github.com/nlohmann/json  
ENV INSTALL_NLOHMANN_JSON=TRUE  
  
# LibreSSL - https://www.libressl.org  
# either LibreSSL or OpenSSL can be installed  
ENV INSTALL_LIBRESSL=TRUE  
  
# OpenSSL - https://www.openssl.org  
# either LibreSSL or OpenSSL can be installed  
ENV INSTALL_OPENSSL=FALSE  
  
# OpenLDAP - http://www.openldap.org  
# requires LibreSSL / OpenSSL  
ENV INSTALL_OPENLDAP=TRUE  
  
# MySQL C-Connector - https://dev.mysql.com/downloads/connector/c/  
ENV INSTALL_MYSQLCLIENT=TRUE  
  
# SQLite 3 - https://sqlite.org  
ENV INSTALL_SQLITE3=TRUE  
  
# SOCI - https://github.com/SOCI/soci  
# requires Boost and MySQL C-Connector and/or SQLite3  
ENV INSTALL_SOCI=TRUE  
  
# C++ REST SDK - https://github.com/Microsoft/cpprestsdk  
# requires Boost / LibreSSL or OpenSSL  
ENV INSTALL_CPP_REST_SDK=TRUE  
  
# Crypto++ Library - https://cryptopp.com  
ENV INSTALL_CRYPTOPP=TRUE  
  
# plustache - {{mustaches}} for C++ - https://github.com/mrtazz/plustache  
ENV INSTALL_PLUSTACHE=TRUE  
  
# nats Library for C - https://github.com/nats-io/cnats  
# requires OpenSSL / LibreSSL  
ENV INSTALL_CNATS=TRUE  
  

