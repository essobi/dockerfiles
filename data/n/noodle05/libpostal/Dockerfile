FROM ubuntu:xenial  
MAINTAINER Wei Gao<wei@gaofmaily.org>  
  
ADD docker-entrypoint.sh /  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
libsnappy1v5 curl ca-certificates \  
libsnappy-dev autoconf automake libtool pkg-config git \  
&& cd /usr/local/src/ \  
&& git clone https://github.com/openvenues/libpostal.git \  
&& cd libpostal \  
## Somehow libpostal complain about following missing configuration  
&& echo "ACLOCAL_AMFLAGS = -I m4" >> Makefile.am \  
&& echo "AC_CONFIG_MACRO_DIR([m4])" >> configure.ac \  
&& mkdir m4 \  
## Don't download data file now.  
# && sed -i -e
"s/\(\s*\.\/libpostal_data\s*download\s*all\s*\$(datadir)\/libpostal\)/#\1/g"
src/Makefile.am \  
&& sed -i -e
's/\(\s*.*\/libpostal_data\s*download\s*all\s*\$(datadir)\/libpostal\)/#\1/g'
src/Makefile.am \  
&& ./bootstrap.sh \  
&& ./configure --prefix=/usr --datadir=/data \  
&& make -j \  
&& make install \  
&& cd / \  
&& rm -fr /usr/local/src/libpostal \  
&& DEBIAN_FRONTEND=noninteractive apt-get remove -y --purge --auto-remove ca-
certificates libsnappy-dev \  
autoconf automake libtool pkg-config git \  
&& DEBIAN_FRONTEND=noninteractive apt-get clean all \  
&& ldconfig \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME [ "/data" ]  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

