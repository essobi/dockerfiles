FROM aadl/cups  
  
MAINTAINER William Weiskopf <william@weiskopf.me>  
  
ENV
DRIVER_URL='http://gdlp01.c-wss.com/gds/0/0100003440/12/Linux_UFRII_PrinterDriver_V330_us_EN.tar.gz'  
RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get -y install \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl $DRIVER_URL | tar xz  
  
RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get -y install \  
autoconf \  
automake \  
#gcc-libs \  
#libgcc1 \  
libglade2-0 \  
libpango1.0-0 \  
libpng16-16 \  
#libxml2 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /tmp  
RUN cd Linux_UFRII_PrinterDriver*/64-bit_Driver/Debian \  
&& dpkg -i *common*.deb  
RUN cd Linux_UFRII_PrinterDriver*/64-bit_Driver/Debian \  
&& dpkg --force-all -i *ufr2*.deb  
  

