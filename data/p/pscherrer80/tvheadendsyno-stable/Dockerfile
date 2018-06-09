#add tvheadend  
FROM phusion/baseimage:0.9.17  
MAINTAINER pscherrer80 <pscherrer80@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Install dependencies, build and install tvheadend  
RUN apt-get update -qq  
RUN apt-get install -qy --no-install-recommends \  
build-essential pkg-config libssl-dev git bzip2 wget cmake\  
libavahi-client-dev zlib1g-dev libcurl4-gnutls-dev python \  
liburiparser1 liburiparser-dev gettext \  
libhdhomerun-dev dvb-apps \  
libarchive-zip-perl libdata-dump-perl libdate-manip-perl libdatetime-format-
iso8601-perl libdatetime-format-strptime-perl \  
libdatetime-perl libdatetime-timezone-perl libhtml-parser-perl libhtml-
tableextract-perl libhtml-tree-perl \  
libhttp-cache-transparent-perl libio-compress-perl libio-stringy-perl libjson-
perl libparse-recdescent-perl \  
libsoap-lite-perl libterm-readkey-perl libtext-bidi-perl libtext-iconv-perl
libwww-mechanize-perl \  
libwww-perl libxml-dom-perl libxml-libxml-perl libxml-libxslt-perl libxml-
parser-perl libxml-twig-perl \  
libxml-writer-perl libxmltv-perl perl perl-modules libxml-treepp-perl
liblingua-en-numbers-ordinate-perl  
  
#####################################  
# Compile and install #  
# tvheadend #  
#####################################  
WORKDIR /tmp/  
RUN git clone https://github.com/tvheadend/tvheadend.git  
WORKDIR /tmp/tvheadend  
RUN git checkout dc6bd3a3  
ADD Makefile.ffmpeg /tmp/tvheadend/Makefile.ffmpeg  
RUN ./configure --enable-libffmpeg_static  
RUN make  
RUN make install  
  
EXPOSE 9981 9982  
VOLUME /config \  
/recordings \  
/data  
  
# add a user to run as non root  
RUN adduser --disabled-password --gecos '' hts  
  
#Start tvheadend when container starts  
RUN mkdir -p /etc/service/tvheadend  
ADD tvheadend /etc/service/tvheadend/run  
RUN chmod +x /etc/service/tvheadend/run  
  
#Add ffmpeg to /usr/bin/  
ADD ffmpeg.gz /usr/bin/  
RUN gunzip /usr/bin/ffmpeg.gz  
RUN chmod a+x /usr/bin/ffmpeg  
  
#Add ffpipe.sh to /usr/local/bin/  
ADD ffpipe.sh /usr/local/bin/  
RUN chmod a+x /usr/local/bin/ffpipe.sh  
  
#Add XMLTV to use other grabber  
#Use mythbuntu repo 'cause ubuntu repo is to old  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ precise main
universe"  
RUN apt-get update -qq  
RUN apt-get install -qy xmltv  

