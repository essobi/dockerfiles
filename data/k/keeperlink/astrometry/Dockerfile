FROM ubuntu  
MAINTAINER Sergei Goshko <serge@keeperlink.com>  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
file \  
gcc \  
git \  
libbz2-dev \  
libcairo2-dev \  
libcfitsio-dev \  
libjpeg-dev \  
libnetpbm10 \  
libnetpbm10-dev \  
libpng12-dev \  
libz-dev \  
make \  
nano \  
netpbm \  
pkg-config \  
pyfits-utils \  
python \  
python-dev \  
python-numpy \  
python-pyfits \  
swig \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -x \  
&& cd /tmp \  
&& git clone https://github.com/dstndstn/astrometry.net \  
&& cd astrometry.net* \  
&& echo "NETPBM_INC=-I/usr/include" > util/makefile.netpbm \  
&& echo "NETPBM_LIB=-L/usr/lib -libnetpbm" >> util/makefile.netpbm \  
&& make \  
&& make py \  
&& make extra \  
&& make install \  
&& cd /tmp \  
&& rm -fr /tmp/astrometry.net*  
  
ENV PATH="/usr/local/astrometry/bin:${PATH}"  
ADD /*.sh /  
RUN set -x \  
&& echo "Testing solve-field..." \  
&& sync \  
&& chmod +x /*.sh \  
&& sync \  
&& /download-data.sh 17 \  
&& solve-field --overwrite /usr/local/astrometry/examples/apod4.jpg  
  
VOLUME ["/usr/local/astrometry/data"]  
  
ENTRYPOINT ["/entry.sh"]  

