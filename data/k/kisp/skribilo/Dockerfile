FROM debian:8.1  
RUN apt-get update && apt-get install -y build-essential git \  
guile-2.0 guile-2.0-dev guile-2.0-libs \  
autoconf gettext \  
gperf texinfo \  
graphicsmagick-imagemagick-compat  
  
RUN git clone git://git.sv.gnu.org/skribilo.git  
RUN git clone git://git.sv.gnu.org/guile-reader.git  
  
WORKDIR /guile-reader  
RUN autoreconf -i || automake; touch build-aux/config.rpath; autoreconf  
RUN ./configure --prefix=/usr --with-guilemoduledir=/usr/share/guile/2.0  
RUN make && make install  
  
WORKDIR /skribilo  
RUN autoreconf -i  
RUN ./configure --prefix=/usr --with-guilemoduledir=/usr/share/guile/site/2.0
--disable-rpath  
  
RUN rm -r doc/*  
RUN echo 'all:' >doc/Makefile  
RUN echo 'install:' >>doc/Makefile  
  
RUN make && make install  

