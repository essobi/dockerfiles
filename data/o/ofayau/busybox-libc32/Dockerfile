FROM progrium/busybox  
  
MAINTAINER Olivier Fayau  
  
#  
# Download & unpack "libc32 for amd64" debian package.  
# see https://packages.debian.org/jessie/libc6-i386  
#  
RUN LIBC32_DEB=libc6-i386_2.19-22_amd64.deb \  
&& wget "http://ftp.fr.debian.org/debian/pool/main/g/glibc/$LIBC32_DEB" \  
&& echo "a448afb85629b2ac0c544dafc515d187 $LIBC32_DEB" | md5sum -c - \  
&& ar p $LIBC32_DEB data.tar.xz | unxz | tar -x \  
&& rm -rf $LIBC32_DEB /usr/share/doc/libc6-i386 /usr/lib32/gconv
/usr/share/lintian  
  
#  
# Download & unpack "lib32gcc1 for amd64" debian package.  
# see https://packages.debian.org/jessie/lib32gcc1  
#  
RUN LIBGCC32_DEB=lib32gcc1_4.9.2-10_amd64.deb \  
&& wget "http://ftp.fr.debian.org/debian/pool/main/g/gcc-4.9/$LIBGCC32_DEB" \  
&& echo "18fe3023cc1e0fbcfcfd261cc2afa013 $LIBGCC32_DEB" | md5sum -c - \  
&& ar p $LIBGCC32_DEB data.tar.xz | unxz | tar -x \  
&& rm -rf $LIBGCC32_DEB /usr/share/doc  
  

