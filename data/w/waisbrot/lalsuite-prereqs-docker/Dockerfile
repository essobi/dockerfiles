FROM ringo/scientific:6.5  
MAINTAINER Nathaniel Waisbrot <code@waisbrot.net>  
  
RUN yum -y groupinstall "Development Tools" "Development Libraries"  
RUN yum install -y zlib-devel fftw-devel  
  
# GSL (latest version is not in RPM)  
RUN mkdir -p /opt/gsl/src \  
&& cd /opt/gsl/src \  
&& wget http://mirrors.ibiblio.org/gnu/ftp/gnu/gsl/gsl-1.16.tar.gz -O - \  
| tar xzf - \  
&& cd /opt/gsl/src/gsl-1.16  
&& ./configure \  
&& make \  
&& make install  
  
# FrameL  
RUN mkdir -p /opt/framel/src \  
&& cd /opt/framel/src/ \  
&& wget http://lappweb.in2p3.fr/virgo/FrameL/libframe-8.21.tar.gz -O - \  
| tar xzf - \  
&& cd /opt/framel/src/libframe-8.21 \  
&& ./configure \  
&& make \  
&& make install  
  
# MetaIO  
RUN mkdir -p /opt/metaio/src \  
&& cd /opt/metaio/src \  
&& wget https://www.lsc-
group.phys.uwm.edu/daswg/download/software/source/metaio-8.3.0.tar.gz -O - \  
| tar xzf - \  
&& cd /opt/metaio/src/metaio-8.3.0 \  
&& ./configure \  
&& make \  
&& make install  
  
ENV
PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig:/usr/lib/pkgconfig:/usr/lib64/pkgconfig  
ENV LD_LIBRARY_PATH=/usr/local/lib  

