FROM maksim77/base  
MAINTAINER Maksim Syomochkin <maksim77ster@gmail.com>  
  
ADD
http://sourceforge.net/projects/minidlna/files/latest/download?source=files
/opt/minidlnad.tar.gz  
COPY minidlnad.conf /etc/  
RUN apt-get update && \  
apt-get install -y gcc \  
make \  
gettext \  
libavutil-dev \  
libavcodec-dev \  
libavformat-dev \  
libjpeg-dev \  
libsqlite3-dev \  
libexif-dev \  
libid3tag0-dev \  
libogg-dev \  
libvorbis-dev \  
libFLAC-dev && \  
apt-get clean  
RUN cd /opt/ && tar xzvf minidlnad.tar.gz && \  
cd /opt/minidlna-*/ && \  
./configure && make && make install && \  
cd / && rm -rf /opt/minidlna-*/ && \  
apt-get purge -y --auto-remove gcc make gettext  
EXPOSE 8200  
VOLUME /data  
ENTRYPOINT ["minidlnad","-f","/etc/minidlnad.conf","-d","-R"]  

