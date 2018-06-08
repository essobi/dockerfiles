FROM ubuntu  
  
#cmtk  
RUN apt-get -qq -y update \  
&& apt-get -qq -y install cmtk python python-pip python-dev build-essential
git nano autoconf nasm automake autoconf m4 libtool bison cmake flex \  
&& pip install --upgrade virtualenv \  
&& pip install --upgrade pip  
  
#python nrrd support  
RUN pip install pynrrd  
  
#woolz  
RUN apt-get -y install build-essential gcc make wget libdirectfb-dev libjpeg-
dev zlib1g-dev libsdl-gfx1.2-dev gcc libsdl1.2-dev libasound2-dev pkg-config
libpci-dev dh-autoreconf csh  
  
ENV MA=/opt/MouseAtlas  
ENV PATH=/opt/MouseAtlas/bin:$PATH  
ENV LD_LIBRARY_PATH=/opt/MouseAtlas/lib:$LD_LIBRARY_PATH  
ENV LD_RUN_PATH=/opt/MouseAtlas/lib:$LD_RUN_PATH  
  
RUN cd /tmp/ \  
&& git clone https://github.com/ma-tech/External.git  
  
RUN cd /tmp/External/ \  
&& cd Fcgi/ \  
&& tar -zxf fcgi-2.4.0.tar.gz \  
&& patch -p0 < fcgi-2.4.0-patch-01 \  
&& cd fcgi-2.4.0 \  
&& ./configure --prefix=$MA \--enable-static --disable-shared \  
&& make \  
&& make install  
  
RUN cd /tmp/External/ \  
&& cd Log4Cpp \  
&& rm -rf log4cpp-1.0 \  
&& tar -zxf log4cpp-1.0.tar.gz \  
&& patch -p0 < log4cpp-1.0.patch \  
&& cd log4cpp-1.0 \  
&& ./configure --prefix $MA \--disable-shared --enable-static --with-pic \  
&& make \  
&& make install  
  
RUN cd /tmp/External/ \  
&& cd PNG \  
&& rm -rf libpng-1.6.29 \  
&& tar -zxf libpng-1.6.29.tar.gz \  
&& cd libpng-1.6.29 \  
&& ./configure --prefix $MA \--disable-shared --enable-static --with-pic \  
&& make \  
&& make install  
  
RUN cd /tmp/External/ \  
&& cd Jpeg \  
&& rm -rf libjpeg-turbo-1.5.1 \  
&& tar -zxf libjpeg-turbo-1.5.1.tar.gz \  
&& cd libjpeg-turbo-1.5.1 \  
&& autoreconf -fi \  
&& ./configure --prefix $MA \--disable-shared --enable-static --with-jpeg7
--with-pic \  
&& make \  
&& make install  
  
RUN cd /tmp/External/ \  
&& cd Tiff \  
&& rm -rf tiff-4.0.8 \  
&& tar -zxf tiff-4.0.8.tar.gz \  
&& cd tiff-4.0.8 \  
&& ./configure --prefix=$MA \--disable-shared --enable-static --with-pic
--with-jpeg-include-dir=$MA/include --with-jpeg-lib-dir==$MA/lib \  
&& make \  
&& make install  
  
RUN cd /tmp/External/ \  
&& cd NIfTI \  
&& tar -zxf nifticlib-2.0.0.tar.gz \  
&& cmake nifticlib-2.0.0 \  
&& make \  
&& make install  
  
RUN cd /tmp/ \  
&& git clone https://github.com/ma-tech/Woolz.git \  
&& cd Woolz \  
&& mkdir -p m4 \  
&& libtoolize \  
&& aclocal \  
&& automake --add-missing \  
&& autoreconf -i --force \  
&& ./build.sh \  
&& ./configure --prefix=$MA \--enable-optimise --enable-extff --with-jpeg=$MA
\--with-tiff=$MA \--with-nifti=/usr/local/ \  
&& make \  
&& make install  
  
RUN cd /opt/ \  
&& git clone https://github.com/Robbie1977/NRRDtools.git  
RUN cd /opt/ \  
&& git clone https://github.com/Robbie1977/SWCtools.git  
RUN cd /opt/ \  
&& git clone https://github.com/Robbie1977/Bound.git  
RUN cd /opt/ \  
&& git clone https://github.com/Robbie1977/3DwarpScoring.git  
RUN cd /opt/ \  
&& git clone https://github.com/Robbie1977/IndexStackConv.git  
RUN cd /opt/ \  
&& git clone https://github.com/Robbie1977/3DstackDisplay.git  
RUN cd /opt/ \  
&& git clone https://github.com/Robbie1977/lsm2nrrd.git  
RUN cd /opt/ \  
&& git clone https://github.com/Robbie1977/nrrd2raw.git  
  
RUN mkdir -p /data/ && cd /data/ \  
&& git clone https://github.com/VirtualFlyBrain/DrosAdultVNSdomains.git  
  
RUN cd /data/ \  
&& git clone https://github.com/VirtualFlyBrain/DrosAdultBRAINdomains.git  
  
RUN cd /data/ \  
&& git clone https://github.com/VirtualFlyBrain/DrosAdultHalfBRAINdomains.git  
  

