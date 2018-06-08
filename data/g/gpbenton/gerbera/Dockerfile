FROM ubuntu:latest  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y uuid-dev
libexpat1-dev libsqlite3-dev libmysqlclient-dev \  
libmagic-dev libexif-dev libcurl4-openssl-dev \  
libavutil-dev libavcodec-dev libavformat-dev libavdevice-dev \  
libavfilter-dev libavresample-dev libswscale-dev libswresample-dev
libpostproc-dev \  
cmake git g++ wget autoconf build-essential libtool libffmpegthumbnailer-dev  
  
ENV VERSION=1.2.0  
WORKDIR /tmp  
  
RUN apt-get install -y sudo  
RUN useradd gerbera -G sudo  
RUN echo '%sudo ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
USER gerbera  
  
RUN wget https://github.com/gerbera/gerbera/archive/v${VERSION}.tar.gz && tar
-xzvf v${VERSION}.tar.gz  
  
RUN gerbera-${VERSION}/scripts/install-pupnp18.sh  
RUN gerbera-${VERSION}/scripts/install-taglib111.sh  
RUN gerbera-${VERSION}/scripts/install-duktape.sh  
  
RUN mkdir build && cd build && cmake ../gerbera-${VERSION} -DWITH_MAGIC=1
-DWITH_CURL=1 -DWITH_JS=1 \  
-DWITH_TAGLIB=1 -DWITH_AVCODEC=1 -DWITH_FFMPEGTHUMBNAILER=1 -DWITH_EXIF=1 -DWITH_SYSTEMD=0 && make -j4 && sudo make install  
  
WORKDIR /  
  
RUN rm -rf /tmp/* && \  
sudo mkdir -p /media/pictures /media/videos /media/music /home/gerbera && \  
sudo chown gerbera:gerbera /home/gerbera && \  
mkdir -p /home/gerbera/.config/gerbera  
  
VOLUME [ "/media/pictures", "/media/videos", "/media/music",
"/home/gerbera/.config/gerbera" ]  
  
ENTRYPOINT [ "/usr/local/bin/gerbera" ]  

