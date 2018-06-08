FROM alpine:edge AS robotv-build  
MAINTAINER Alexander pipelka <alexander.pipelka@gmail.com>  
  
ARG ROBOTV_VERSION=  
ARG VDR_VERSION=2.3.8  
USER root  
  
RUN echo "http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk update && apk add build-base freetype-dev fontconfig-dev gettext-dev \  
libjpeg-turbo-dev libcap-dev pugixml-dev curl-dev git bzip2 libexecinfo-dev \  
ncurses-dev bash  
  
RUN mkdir -p /build  
WORKDIR /build  
  
RUN echo "building roboTV version '${ROBOTV_VERSION}'"  
  
RUN wget ftp://ftp.tvdr.de/vdr/Developer/vdr-${VDR_VERSION}.tar.bz2  
RUN tar -jxf vdr-${VDR_VERSION}.tar.bz2  
RUN git clone -b ${ROBOTV_VERSION} https://github.com/pipelka/vdr-plugin-
robotv.git vdr-${VDR_VERSION}/PLUGINS/src/robotv  
RUN git clone https://github.com/manio/vdr-plugin-dvbapi.git
vdr-${VDR_VERSION}/PLUGINS/src/dvbapi  
RUN git clone https://github.com/vdr-projects/vdr-plugin-epgsearch.git
vdr-${VDR_VERSION}/PLUGINS/src/epgsearch  
RUN git clone -b robotv https://github.com/pipelka/vdr-plugin-satip.git
vdr-${VDR_VERSION}/PLUGINS/src/satip  
RUN git clone https://github.com/vdr-projects/vdr-plugin-streamdev.git
vdr-${VDR_VERSION}/PLUGINS/src/streamdev  
  
WORKDIR vdr-${VDR_VERSION}  
COPY templates/Make.* /build/vdr-${VDR_VERSION}/  
  
RUN mkdir -p /build/patches  
COPY patches/ /build/patches/  
  
RUN for patch in `ls /build/patches/vdr`; do \  
echo ${patch} ; \  
patch -p1 < /build/patches/vdr/${patch} ; \  
done  
  
WORKDIR PLUGINS/src/epgsearch  
RUN patch -p1 < /build/patches/epgsearch/install-conf.patch  
  
WORKDIR ../../..  
RUN make -j 4  
  
RUN mkdir -p /opt/vdr  
  
RUN make install  
  
RUN for plugin in robotv epgsearch satip streamdev-server ; do \  
strip -s --strip-debug /opt/vdr/lib/libvdr-${plugin}.so.* ; \  
done ; \  
strip -s --strip-debug /opt/vdr/bin/vdr  
  
RUN rm -Rf /opt/vdr/man  
RUN rm -Rf /opt/vdr/locale/*  
  
ENV LIBS="dvbhddevice dvbsddevice epgtableid0 hello osddemo pictures rcu
skincurses status svccli svcsvr svdrpdemo streamdev-client"  
RUN for lib in ${LIBS} ; do \  
echo "removing /opt/vdr/lib/libvdr-$lib" ; \  
rm -f /opt/vdr/lib/libvdr-${lib}* ; \  
done  
  
FROM alpine:edge AS robotv-server  
  
USER root  
  
ENV DVBAPI_ENABLE="0" \  
DVBAPI_HOST="127.0.0.1" \  
DVBAPI_PORT="2000" \  
DVBAPI_OFFSET=0 \  
SATIP_NUMDEVICES="2" \  
SATIP_SERVER="192.168.16.10" \  
ROBOTV_TIMESHIFTDIR="/video" \  
ROBOTV_MAXTIMESHIFTSIZE="4000000000" \  
ROBOTV_PICONSURL= \  
ROBOTV_SERIESFOLDER="Serien" \  
ROBOTV_CHANNELCACHE="true" \  
ROBOTV_EPGIMAGEURL= \  
VDR_LOGLEVEL=2 \  
VDR_UPDATECHANNELS=3 \  
TZ="Europe/Vienna"  
RUN echo "http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk update && apk add freetype fontconfig libintl libexecinfo \  
libjpeg-turbo libcap pugixml libcurl  
  
RUN mkdir -p /opt && \  
mkdir -p /data && \  
mkdir -p /video && \  
mkdir -p /opt/templates && \  
mkdir -p /timeshift  
  
COPY \--from=robotv-build /opt/ /opt/  
COPY bin/runvdr.sh /opt/vdr/  
COPY templates/diseqc.conf /opt/templates/  
COPY templates/sources.conf /opt/templates/  
COPY templates/channels.conf /opt/templates/  
  
RUN chmod +x /opt/vdr/runvdr.sh  
  
ENTRYPOINT [ "/opt/vdr/runvdr.sh" ]  

