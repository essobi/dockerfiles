# UQM-crossbuilder  
FROM ubuntu:quantal  
MAINTAINER jorisvddonk@gmail.com  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu quantal main universe" >
/etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository "deb http://archive.ubuntu.com/ubuntu quantal main universe
restricted multiverse" && \  
apt-get install -y build-essential mingw-w64-i686-dev binutils-mingw-w64-i686
gcc-mingw-w64-base gcc-mingw-w64-i686 g++-mingw-w64-i686 pkg-config dos2unix
wget  
  
  
RUN mkdir -p /usr/i686-w64-mingw32/bin && \  
ln -s /usr/bin/i686-w64-mingw32-addr2line /usr/i686-w64-mingw32/bin/addr2line
&& \  
ln -s /usr/bin/i686-w64-mingw32-ar /usr/i686-w64-mingw32/bin/ar && \  
ln -s /usr/bin/i686-w64-mingw32-as /usr/i686-w64-mingw32/bin/as && \  
ln -s /usr/bin/i686-w64-mingw32-c++ /usr/i686-w64-mingw32/bin/c++ && \  
ln -s /usr/bin/i686-w64-mingw32-c++filt /usr/i686-w64-mingw32/bin/c++filt && \  
ln -s /usr/bin/i686-w64-mingw32-cpp /usr/i686-w64-mingw32/bin/cpp && \  
ln -s /usr/bin/i686-w64-mingw32-dlltool /usr/i686-w64-mingw32/bin/dlltool && \  
ln -s /usr/bin/i686-w64-mingw32-dllwrap /usr/i686-w64-mingw32/bin/dllwrap && \  
ln -s /usr/bin/i686-w64-mingw32-elfedit /usr/i686-w64-mingw32/bin/elfedit && \  
ln -s /usr/bin/i686-w64-mingw32-g++ /usr/i686-w64-mingw32/bin/g++ && \  
ln -s /usr/bin/i686-w64-mingw32-gcc /usr/i686-w64-mingw32/bin/gcc && \  
ln -s /usr/bin/i686-w64-mingw32-gcc-4.6 /usr/i686-w64-mingw32/bin/gcc-4.6 && \  
ln -s /usr/bin/i686-w64-mingw32-gcov /usr/i686-w64-mingw32/bin/gcov && \  
ln -s /usr/bin/i686-w64-mingw32-gprof /usr/i686-w64-mingw32/bin/gprof && \  
ln -s /usr/bin/i686-w64-mingw32-ld /usr/i686-w64-mingw32/bin/ld && \  
ln -s /usr/bin/i686-w64-mingw32-ld.bfd /usr/i686-w64-mingw32/bin/ld.bfd && \  
ln -s /usr/bin/i686-w64-mingw32-ld.nm /usr/i686-w64-mingw32/bin/ld.nm && \  
ln -s /usr/bin/i686-w64-mingw32-objcopy /usr/i686-w64-mingw32/bin/objcopy && \  
ln -s /usr/bin/i686-w64-mingw32-objdump /usr/i686-w64-mingw32/bin/objdump && \  
ln -s /usr/bin/i686-w64-mingw32-ranlib /usr/i686-w64-mingw32/bin/ranlib && \  
ln -s /usr/bin/i686-w64-mingw32-readelf /usr/i686-w64-mingw32/bin/readelf && \  
ln -s /usr/bin/i686-w64-mingw32-size /usr/i686-w64-mingw32/bin/size && \  
ln -s /usr/bin/i686-w64-mingw32-strings /usr/i686-w64-mingw32/bin/strings && \  
ln -s /usr/bin/i686-w64-mingw32-strip /usr/i686-w64-mingw32/bin/strip && \  
ln -s /usr/bin/i686-w64-mingw32-windmc /usr/i686-w64-mingw32/bin/windmc && \  
ln -s /usr/bin/i686-w64-mingw32-windres /usr/i686-w64-mingw32/bin/windres && \  
ln -s /usr/i686-w64-mingw32/libogg.lib /usr/i686-w64-mingw32/lib/ogg.lib && \  
ln -s /usr/i686-w64-mingw32/libogg_d.lib /usr/i686-w64-mingw32/lib/ogg_d.lib
&& \  
ln -s /usr/i686-w64-mingw32/libogg_static.lib
/usr/i686-w64-mingw32/lib/ogg_static.lib && \  
ln -s /usr/i686-w64-mingw32/libogg_static_d.lib
/usr/i686-w64-mingw32/lib/ogg_static_d.lib && \  
ln -s /usr/i686-w64-mingw32/libvorbis.lib /usr/i686-w64-mingw32/lib/vorbis.lib
&& \  
ln -s /usr/i686-w64-mingw32/libvorbis_d.lib
/usr/i686-w64-mingw32/lib/vorbis_d.lib && \  
ln -s /usr/i686-w64-mingw32/libvorbis_static.lib
/usr/i686-w64-mingw32/lib/vorbis_static.lib && \  
ln -s /usr/i686-w64-mingw32/libvorbis_static_d.lib
/usr/i686-w64-mingw32/lib/vorbis_static_d.l && \  
ln -s /usr/i686-w64-mingw32/libvorbisfile.lib
/usr/i686-w64-mingw32/lib/vorbisfile.lib && \  
ln -s /usr/i686-w64-mingw32/libvorbisfile_d.lib
/usr/i686-w64-mingw32/lib/vorbisfile_d.lib && \  
ln -s /usr/i686-w64-mingw32/libvorbisfile_static.lib
/usr/i686-w64-mingw32/lib/vorbisfile_static.lib && \  
ln -s /usr/i686-w64-mingw32/libvorbisfile_static_d.lib
/usr/i686-w64-mingw32/lib/vorbisfile_static_d.lib  
  
RUN mkdir -p /uqmdev/scripts/crossbuild && \  
mkdir -p /uqmdev/project  
# Upload crossbuilder scripts to the container  
ADD ./scripts/ /uqmdev/scripts/  
ADD ./scripts/crossbuild/ /uqmdev/scripts/crossbuild/  
# Fix line endings on some shell scripts. Just in case you're using git on
windows with autocrlf set to true :)  
RUN dos2unix /uqmdev/scripts/*.sh && \  
dos2unix /uqmdev/scripts/crossbuild/*.sh  
# Build UQM dependencies..  
RUN /uqmdev/scripts/build-uqm-dependencies.sh  
# Set up entrypoint, working directory, default command and mark /uqm as being
a volume which needs to be bound later..  
WORKDIR /uqm  
VOLUME ["/uqm"]  
CMD ["uqm"]  
ENTRYPOINT ["/bin/bash", "/uqmdev/scripts/cross-build.sh"]  

