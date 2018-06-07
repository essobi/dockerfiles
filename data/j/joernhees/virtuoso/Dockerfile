FROM debian  
MAINTAINER Joern Hees  
  
ENV VIRTUOSO_VERSION=7.2.4.2  
ENV VIRTUOSO_SOURCE=https://github.com/openlink/virtuoso-
opensource/releases/download/v$VIRTUOSO_VERSION/virtuoso-
opensource-$VIRTUOSO_VERSION.tar.gz  
  
ARG BUILD_DIR=/tmp/build  
ARG VIRTUOSO_DEB_PKG_DIR=/virtuoso_deb  
ARG BUILD_ARGS=""  
  
RUN \  
# remember installed packages for later cleanup  
dpkg \--get-selections > /inst_packages.dpkg \  
  
# install build essentials  
&& apt-get update && apt-get install -y \  
build-essential \  
devscripts \  
wget \  
  
# download and extract virtuoso source  
&& mkdir -p "$BUILD_DIR" \  
&& cd "$BUILD_DIR" \  
&& echo -n "downloading..." \  
&& wget -nv "$VIRTUOSO_SOURCE" \  
&& echo " done." \  
&& echo -n "extracting..." \  
&& tar -xaf virtuoso*.tar* \  
&& rm virtuoso*.tar* \  
&& echo " done." \  
  
# build debian packages for virtuoso  
&& cd "$BUILD_DIR"/virtuoso-opensource*/ \  
&& mk-build-deps -irt'apt-get \--no-install-recommends -yV' \  
&& dpkg-checkbuilddeps \  
&& dpkg-buildpackage -us -uc $BUILD_ARGS \  
  
# additionally build dbpedia vad file  
&& ./configure \--with-layout=debian \--enable-dbpedia-vad \  
&& cd binsrc \  
&& make $BUILD_ARGS \  
&& cp dbpedia/dbpedia_dav.vad ../../ \  
  
# make virtuoso packages available for apt  
&& cd "$BUILD_DIR" \  
&& rm -r virtuoso-opensource*/ \  
&& (dpkg-scanpackages ./ | gzip > Packages.gz) \  
&& echo "deb file:$BUILD_DIR ./" >> /etc/apt/sources.list.d/virtuoso.list \  
  
# cleanup packages and caches for building virtuoso (reduce container size)  
&& dpkg \--clear-selections \  
&& dpkg \--set-selections < /inst_packages.dpkg \  
&& rm /inst_packages.dpkg \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get -y dselect-upgrade \  
  
# install virtuoso with runtime dependencies via apt and  
# move dbpedia vad file into shared location  
&& apt-get update && apt-get install -y \--force-yes \  
virtuoso-server \  
virtuoso-vad-bpel \  
virtuoso-vad-conductor \  
virtuoso-vad-demo \  
virtuoso-vad-doc \  
virtuoso-vad-isparql \  
virtuoso-vad-ods \  
virtuoso-vad-rdfmappers \  
virtuoso-vad-sparqldemo \  
virtuoso-vad-syncml \  
virtuoso-vad-tutorial \  
&& mv $BUILD_DIR/dbpedia_dav.vad /usr/share/virtuoso-opensource-7/vad/ \  
  
# remove virtuoso packages and apt cache (small container size)  
&& rm -rf $BUILD_DIR \  
&& rm /etc/apt/sources.list.d/virtuoso.list \  
&& rm -rf /var/lib/apt/lists/* \  
  
# allow virtuoso to access the /import DIR in container  
&& sed -i '/^DirsAllowed\s*=/ s_\s*$_, /import_' /etc/virtuoso-
opensource-7/virtuoso.ini \  
  
# init db folder  
&& /etc/init.d/virtuoso-opensource-7 start \  
&& /etc/init.d/virtuoso-opensource-7 stop \  
# sadly the above doesn't really wait for DB shutdown... give it 30 more
seconds  
&& sleep 30 \  
  
# back init state up to init empty mounted DB volume in start.sh  
&& cp -a /var/lib/virtuoso-opensource-7 /var/lib/virtuoso-opensource-7.orig  
  
VOLUME "/var/lib/virtuoso-opensource-7" "/import"  
  
EXPOSE 1111 8890  
  
# you can override the following default values via env vars and start.sh will  
# replace them in the virtuoso.ini:  
# ENV NumberOfBuffers=10000 MaxDirtyBuffers=6000 MaxCheckpointRemap=2000  
  
COPY ./README.md /root/README_VIRTUOSO.md  
COPY ./start.sh ./wait_ready /usr/local/sbin/  
ENTRYPOINT ["/usr/local/sbin/start.sh"]  
  

