FROM centos:7  
MAINTAINER Louis Trezzini <louis.trezzini@ponts.org>  
  
RUN groupadd python && useradd -g python python  
  
RUN mkdir /app && chown python:python /app && chmod 700 /app  
RUN mkdir /uploads && chown python:python /uploads && chmod 700 /uploads  
RUN mkdir /logs && chown python:python /logs && chmod 700 /logs  
  
WORKDIR /app  
  
RUN echo \  
&& yum check-update --disableplugin=fastestmirror || true \  
&& yum -y install https://centos7.iuscommunity.org/ius-release.rpm \  
&& yum -y install python36u python36u-devel python36u-pip \  
&& yum -y install hdf5 ghostscript gcc make autoconf-archive automake
pkgconfig \  
ImageMagick wget gcc-c++ unzip libtool libtiff-devel libpng-devel libjpeg-
turbo-devel zlib-devel  
  
RUN mkdir /deps && cd /deps && wget
https://github.com/DanBloomberg/leptonica/releases/download/1.74.4/leptonica-1.74.4.tar.gz
\  
&& tar -xvf leptonica-1.74.4.tar.gz && cd leptonica-1.74.4/ \  
&& ./configure --prefix=/usr --with-libtiff && make -j $(nproc) && make
install \  
&& rm -rf /deps  
  
ENV PKG_CONFIG_PATH=/usr/lib/pkgconfig  
  
RUN mkdir /deps && cd /deps && wget https://github.com/tesseract-
ocr/tesseract/archive/eba0ae3b88a46a93e981770caa0b148d65cc4468.zip \  
&& unzip eba0ae3b88a46a93e981770caa0b148d65cc4468.zip -d tesseract/ && cd
tesseract/tesseract-eba0ae3b88a46a93e981770caa0b148d65cc4468/ \  
&& ./autogen.sh && ./configure && make -j $(nproc) && make install \  
&& rm -rf /deps  
  
RUN pip3.6 install numpy  
RUN pip3.6 install opencv-python==3.3.0.10  
COPY requirements.txt requirements.txt  
RUN pip3.6 install -r requirements.txt  
  
ENV PATH="/usr/bin:${PATH}" LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/lib"
TESSDATA_PREFIX=/usr/share/tessdata  
  
# Install trained lang data  
RUN mkdir -p $TESSDATA_PREFIX  
COPY franceocr.traineddata $TESSDATA_PREFIX  
COPY OCRB.traineddata $TESSDATA_PREFIX  
  
COPY . /app  
  
USER python  
  
EXPOSE 5000  
ENTRYPOINT ["gunicorn", "--config", "/app/gunicorn.conf", "--log-config",
"/app/logging.conf", "-b", ":5000", "server:server"]  

