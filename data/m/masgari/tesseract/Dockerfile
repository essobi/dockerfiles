FROM masgari/thrift  
  
MAINTAINER Mamad Asgari <mammad.asgari@gmail.com>  
  
# non interactive apt  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV TESSERACT_VERSION 3.02.02  
ENV TESSDATA_VERSION 3.02  
ENV TESSDATA_OSD 3.01.osd  
  
ENV DATA_FOLDER /usr/local/share/tessdata  
ENV HEADER_FOLDER /usr/local/include/tesseract  
  
# Install required packages  
RUN apt-get -q -y update \  
&& apt-get -q -y -f install autoconf automake libtool libpng12-dev
libjpeg62-dev \  
libgif-dev zlib1g-dev  
  
RUN apt-get -q -y install libtiff4-dev libleptonica-dev libboost-thread-dev  
  
# Download files  
RUN mkdir /opt/tesseract && cd /opt/tesseract \  
&& curl https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-$TESSERACT_VERSION.tar.gz | tar -xz \  
&& curl https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-$TESSDATA_VERSION.eng.tar.gz | tar -xz \  
&& curl https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-$TESSDATA_OSD.tar.gz | tar -xz  
  
# Compile Tesseract  
RUN cd /opt/tesseract/tesseract-ocr \  
&& ./autogen.sh && ./configure && make && make install && ldconfig  
  
RUN cd /opt/tesseract/tesseract-ocr/ccstruct \  
&& cp blobs.h $HEADER_FOLDER \  
&& cp ipoints.h $HEADER_FOLDER \  
&& cp points.h $HEADER_FOLDER \  
&& cp rect.h $HEADER_FOLDER \  
&& cp vecfuncs.h $HEADER_FOLDER \  
&& cd ../ccutil \  
&& cp clst.h $HEADER_FOLDER \  
&& cp elst.h $HEADER_FOLDER \  
&& cp lsterr.h $HEADER_FOLDER \  
&& cp mfcpch.h $HEADER_FOLDER \  
&& cp notdll.h $HEADER_FOLDER \  
&& cp tprintf.h $HEADER_FOLDER \  
&& cd .. \  
&& cp ccmain/osdetect.h $HEADER_FOLDER \  
&& cp viewer/scrollview.h $HEADER_FOLDER  
  
# Copy Tesseract models  
RUN cd /opt/tesseract \  
&& cp tesseract-ocr/tessdata/eng.* $DATA_FOLDER \  
&& cp tesseract-ocr/tessdata/osd.traineddata $DATA_FOLDER  
  
# Cleanup  
RUN cd / && rm -fr /opt/tesseract \  
&& apt-get -q -y clean && rm -rf /var/cache/apt/archives/*
/var/lib/apt/lists/* && rm -fr /tmp/*  
  
CMD ["/usr/local/bin/tesseract", "--help"]  

