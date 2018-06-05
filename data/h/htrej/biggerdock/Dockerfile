#Dockerfile to build a pdf2htmlEX image with its dependencies and beneficial
supplements  
  
#Dockerfile  
  
FROM phusion/baseimage:0.9.18  
  
MAINTAINER YangRY  
  
WORKDIR /root/build  
  
ENV PKG_CONFIG_PATH /usr/lib/pkgconfig:/usr/lib/x86_64-linux-
gnu/pkgconfig:/usr/share/pkgconfig:/root/build/pkgconfig/root/build/pkg-
config/check/pkgconfig  
  
RUN sudo echo "deb http://archive.ubuntu.com/ubuntu trusty-backports main
restricted universe multiverse" >> /etc/apt/sources.list && \  
sudo printf "Package: *\nPin: release a=trusty-backports\nPin-Priority: 500"
>> /etc/apt/preferences && \  
LC_ALL=C.UTF-8 add-apt-repository -y ppa:cz.nic-labs/knot-dns && \  
add-apt-repository -y ppa:george-edison55/cmake-3.x && \  
add-apt-repository -y ppa:cjwatson/launchpad && \  
add-apt-repository -y ppa:richardpuppy96/backports && \  
add-apt-repository -y ppa:fontforge/fontforge && \  
sudo apt-get update && \  
sudo apt-get upgrade -y && \  
sudo apt-get install -y \  
apt-build \  
apt-file \  
auto-apt \  
autoconf \  
automake \  
autotools-dev \  
bison \  
build-essential \  
bzip2 \  
checkinstall \  
chrpath \  
cmake \  
curl \  
default-jdk \  
default-jre \  
dos2unix \  
flex \  
fontconfig \  
fontforge \  
ghostscript \  
giflib-tools \  
gir1.2-poppler-0.18 \  
git \  
git-svn \  
gobject-introspection \  
gperf \  
gtk-doc-tools \  
icu-devtools \  
libcroco-tools \  
libcroco3-dev \  
libcroco3 \  
libffi-dev \  
libffi6 \  
libfontconfig1-dev \  
libfontforge-dev \  
libfreetype6 \  
libfreetype6-dev \  
libgetopt++-dev \  
libgif-dev \  
libgif7 \  
libharfbuzz-dev \  
libicu-dev \  
libicu52 \  
libjpeg-turbo8-dev \  
libncursesw5-dev \  
libpcre3-dev \  
libpng12-0 \  
libpng12-dev \  
libpoppler58 \  
libpoppler-dev \  
libpoppler-glib8 \  
libpoppler-glib-dev \  
libpoppler-private-dev \  
librsvg2-2 \  
librsvg2-dev \  
libspectre-dev \  
libspectre1 \  
libspiro0 \  
libspiro-dev \  
libtiff5 \  
libtiff5-dev \  
libtiff-tools \  
libtool \  
libxt-dev \  
libxml2 \  
libxml2-dev \  
libxml2-utils \  
locate \  
packaging-dev \  
poppler-utils \  
poppler-data \  
python-dev \  
python-fontforge \  
python2.7-dev \  
ragel \  
realpath \  
tar \  
texinfo \  
ttfautohint \  
unifont \  
uthash-dev \  
uuid-dev \  
wget \  
yasm \  
yodl \  
zlib1g-dev && \  
sudo updatedb && \  
sudo auto-apt updatedb && \  
sudo auto-apt update-local && \  
# printf "Package: *\nPin: release o=LP-PPA-cz.nic-labs-knot-dns\nPin-
Priority: 500" > /etc/apt/preferences.d/cz.nic-labs-knot-dns-pin-400.pref && \  
# printf "\nPackage: gettext autopoint\nPin: release o=LP-PPA-cz.nic-labs-
knot-dns\nPin-Priority: 500" >> /etc/apt/preferences.d/cz.nic-labs-knot-dns-
pin-400.pref && \  
apt-get update && \  
aptitude full-upgrade -y && \  
# sudo ln -snf /bin/bash /bin/sh && \  
# git clone git://git.code.sf.net/p/zsh/code zsh && \  
# cd zsh && \  
# \  
# git checkout $(git describe --tags --always) && \  
# \  
# ./Util/preconfig && \  
# \  
# ./configure \  
# \--bindir=/bin \  
# \--enable-additional-fpath=/usr/share/zsh/vendor-
functions,/usr/share/zsh/vendor-completions \  
# \--enable-cap \  
# \--enable-custom-patchlevel=Debian \  
# \--enable-etcdir=/etc/zsh \  
# \--enable-fndir=/usr/share/zsh/functions \  
# \--enable-function-subdirs \  
# \--enable-maildir-support \  
# \--enable-max-jobtable-size=256 \  
# \--enable-pcre \  
# \--enable-readnullcmd=pager \  
# \--enable-site-fndir=/usr/local/share/zsh/site-functions \  
# \--infodir=/usr/share/info \  
# \--mandir=/usr/share/man \  
# \--prefix=/usr \  
# \--with-tcsetpgrp \  
# \--with-term-lib="ncursesw tinfo" \  
# LDFLAGS="-Wl,--as-needed -g -Wl,-Bsymbolic-functions -Wl,-z,relro" && \  
# \  
# make && \  
# sudo checkinstall \  
# \--default \  
# \--install=yes \  
# \--maintainer="Richard Yang" \  
# \--nodoc \  
# \--pkglicense=MIT \  
# \--pkgname=zsh \  
# \--pkgversion=$(git describe --tags --always | cut -d '-' -f2,3,4) \  
# \--showinstall=no \  
# \--type=debian \  
# \--provides=zsh \  
# \--conflicts=zsh \  
# \--replaces=zsh \  
# make \  
# install \  
# install.info && \  
# sudo echo /bin/zsh >> /etc/shells && \  
# chsh -s /bin/zsh && \  
# ln -snf /bin/zsh /bin/sh  
git clone git://github.com/robbyrussell/oh-my-zsh /root/.oh-my-zsh && \  
cp /root/.oh-my-zsh/templates/zshrc.zsh-template /root/.zshrc && \  
git clone --depth=1 git://github.com/jonathancone/svn-utils && \  
cd svn-utils && \  
chmod +x git-svn-cloneback.sh && \  
chmod +x svn-lookback.sh && \  
sudo cp git-svn-cloneback.sh /usr/bin/git-svn-cloneback.sh && \  
sudo cp svn-lookback.sh /usr/bin/svn-lookback.sh && \  
cd .. && \  
wget -O autodeb.sh http://pastebin.com/raw/f77db4c65 && \  
chmod +x autodeb.sh && \  
dos2unix autodeb.sh && \  
sudo cp autodeb.sh /usr/bin/autodeb && \  
# git clone \--depth=1 git://anongit.freedesktop.org/pkg-config && \  
# cd pkg-config && \  
# ./autogen.sh && \  
# ./configure \  
# \--prefix=/usr \  
# \--with-internal-glib \  
# \--disable-host-tool && \  
# make && \  
# checkinstall \  
# \--conflicts=pkg-config \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--nodoc \  
# \--pkgname=pkg-config \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{11\\}//') \  
# \--provides=pkg-config \  
# \--replaces=pkg-config \  
# \--showinstall=no && \  
# cd /root/build && \  
#RUN git clone git://github.com/atgreen/libffi.git && \  
# cd libffi && \  
# ./autogen.sh && \  
# sed -e '/^includesdir/ s/$(libdir).*$/$(includedir)/' -i include/Makefile.in
&& \  
# sed -e '/^includedir/ s/=.*$/=@includedir@/' -e 's/^Cflags:
-I${includedir}/Cflags:/' -i libffi.pc.in && \  
# ./configure --prefix=/usr && \  
# checkinstall && \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=libffi \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{1\\}//') \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=libffi \  
# \--conflicts=libffi \  
# \--replaces=libffi && \  
# cd .. && \  
# git clone git://git.code.sf.net/p/giflib/code giflib && \  
# cd giflib && \  
# ./autogen.sh --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=giflib \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=giflib,libgif \  
# \--conflicts=giflib,libgif \  
# \--replaces=giflib,libgif && \  
# cd .. && \  
# git clone git://git.gnome.org/libxml2 libxml2 && \  
# cd libxml2 && \  
# ./autogen.sh \  
# \--prefix=/usr \  
# \--with-history && \  
# printf "\n10\n\n4\n1\n6\ncheckinstall\n" | sudo checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=libxml2 \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{1\\}//') \  
# \--requires=pkg-config \  
# \--pkgrelease=1 \  
# \--pkggroup=checkinstall \  
# \--maintainer="Richard Yang" \  
# \--provides=libxml2 \  
# \--conflicts=libxml2 \  
# \--replaces=libxml2 && \  
# cd .. && \  
# git-svn-cloneback.sh -u svn://vcs.exim.org/pcre2/code/trunk -l 1 -o pcre &&
\  
# cd pcre && \  
# ./autogen.sh && \  
# ./configure \  
# \--prefix=/usr \  
# \--enable-unicode-properties \  
# \--enable-pcre2-16 \  
# \--enable-pcre2-32 \  
# \--enable-pcregrep-libbz2 \  
# \--enable-pcregrep-libz && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=pcre \  
# \--pkgversion=$(git svn find-rev $(git log \--max-count 1
--pretty=format:%H)) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=pcre \  
# \--conflicts=pcre \  
# \--replaces=pcre && \  
# cd .. && \  
# git clone git://git.gnome.org/glib && \  
# cd glib && \  
# ./autogen.sh && \  
# ./configure \  
# \--prefix=/usr \  
# \--with-pcre=system && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=glib \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--install=no \  
# \--maintainer="Richard Yang" \  
# \--provides=glib,libglib2.0-dev,libglib2.0-bin \  
# \--conflicts=glib,libglib2.0-dev,libglib2.0-bin \  
# \--replaces=glib,libglib2.0-dev,libglib2.0-bin && \  
# dpkg -i -B glib_$(git describe --tags --always)-1_amd64.deb && \  
# cd .. && \  
# git clone \--depth=1 git://git.gnome.org/libcroco && \  
# cd libcroco && \  
# ./autogen.sh --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=libcroco \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=libcroco \  
# \--conflicts=libcroco \  
# \--replaces=libcroco && \  
# cd ..  
#RUN git clone git://git.gnome.org/gobject-introspection && \  
# cd gobject-introspection && \  
# apt-get install -y python-dev && ./autogen.sh --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=gobject-introspection \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=gobject-introspection \  
# \--conflicts=gobject-introspection \  
# \--replaces=gobject-introspection && \  
# cd .. && \  
# git-svn-cloneback.sh -u http://source.icu-
project.org/repos/icu/icu/trunk/source -l 1 -o icu && \  
# cd icu && \  
# ./configure \  
# \--prefix=/usr \  
# CC=gcc \  
# CXX=g++ && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=icu \  
# \--pkgversion=$(git svn find-rev $(git log \--max-count 1
--pretty=format:%H)) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=libicu,libicu-dev \  
# \--conflicts=libicu,libicu-dev \  
# \--replaces=libicu,libicu-dev && \  
# cd .. && \  
# git clone git://anongit.freedesktop.org/harfbuzz && \  
# cd harfbuzz && \  
# ./autogen.sh && \  
# ./configure \  
# \--prefix=/usr \  
# \--with-gobject && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=harfbuzz \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=harfbuzz,libharfbuzz-dev \  
# \--conflicts=harfbuzz \  
# \--replaces=harfbuzz,libharfbuzz-dev && \  
# cd ..  
#RUN git clone \--depth=1 git://git.code.sf.net/p/libpng/code libpng && \  
# cd libpng && \  
# ./autogen.sh && \  
# ./configure --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=libpng \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{7\\}//') \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=libpng \  
# \--conflicts=libpng \  
# \--replaces=libpng && \  
# cd .. && \  
# git clone git://github.com/yasm/yasm && \  
# cd yasm && \  
# ./autogen.sh && \  
# sed -i 's#) ytasm.*#)#' Makefile.in && \  
# ./configure --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=yasm \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{1\\}//') \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=yasm \  
# \--conflicts=yasm \  
# \--replaces=yasm && \  
# cd .. && \  
# git clone git://github.com/libjpeg-turbo/libjpeg-turbo.git && \  
# cd libjpeg-turbo && \  
# autoreconf -if && \  
# ./configure \  
# \--prefix=/usr \  
# \--with-jpeg8 && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=libjpeg-turbo \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{5\\}//') \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=libjpeg-turbo \  
# \--conflicts=libjpeg-turbo \  
# \--replaces=libjpeg-turbo && \  
# cd .. && \  
# git clone https://github.com/vadz/libtiff && \  
# cd libtiff && \  
# ./configure --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=libtiff \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{9\\}//') \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=libtiff \  
# \--conflicts=libtiff \  
# \--replaces=libtiff && \  
# cd .. && \  
# git clone git://git.gnome.org/gdk-pixbuf && \  
# cd gdk-pixbuf && \  
# ./autogen.sh && \  
# ./configure --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=gdk-pixbuf \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=gdk-pixbuf,libgdk-pixbuf2.0-dev \  
# \--conflicts=gdk-pixbuf,libgdk-pixbuf2.0-dev \  
# \--replaces=gdk-pixbuf,libgdk-pixbuf2.0-dev && \  
# cd .. && \  
# git clone git://git.gnome.org/librsvg && \  
# cd librsvg && \  
# ./autogen.sh && \  
# ./configure --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=librsvg \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=librsvg \  
# \--conflicts=librsvg \  
# \--replaces=librsvg && \  
# cd .. && \  
# git clone git://github.com/mm2/Little-CMS.git && \  
# cd Little-CMS && \  
# ./autogen.sh --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=lcms \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{6\\}//') \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=lcms \  
# \--conflicts=lcms \  
# \--replaces=lcms && \  
# cd .. && \  
# wget http://downloads.sourceforge.net/openjpeg.mirror/openjpeg-1.5.2.tar.gz
&& \  
# tar xf openjpeg-1.5.2.tar.gz && \  
# cd openjpeg-1.5.2 && \  
# autoreconf -if && \  
# ./configure --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=openjpeg \  
# \--pkgversion=1.5.2 \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=openjpeg \  
# \--conflicts=openjpeg \  
# \--replaces=openjpeg && \  
# cd .. && \  
# git clone git://github.com/fontforge/libspiro.git && \  
# cd libspiro && \  
# autoreconf -i && \  
# automake --foreign -Wall && \  
# ./configure --prefix=/usr && \  
# printf "\n0.5.20150702-14-g5381507\n\n" | checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=libspiro \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{1\\}//') \  
# \--maintainer="Richard Yang" \  
# \--provides=libspiro \  
# \--conflicts=libspiro \  
# \--replaces=libspiro && \  
# cd .. && \  
wget
https://bitbucket.org/sortsmill/libunicodenames/downloads/libunicodenames-1.1.0_beta1.tar.xz
&& \  
tar xf libunicodenames-1.1.0_beta1.tar.xz && \  
cd libunicodenames-1.1.0_beta1 && \  
./configure --prefix=/usr && \  
printf "\n1.10-beta1\n\n" | checkinstall \  
\--showinstall=no \  
\--nodoc \  
\--pkgname=libunicodenames \  
\--pkgversion=1.1.0_beta1 \  
\--maintainer="Richard Yang" \  
\--provides=libunicodenames \  
\--conflicts=libunicodenames \  
\--replaces=libunicodenames && \  
cd .. && \  
# git clone git://github.com/fontforge/libuninameslist.git && \  
# cd libuninameslist && \  
# autoreconf -i && \  
# automake && \  
# ./configure --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=libuninameslist \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=libuninameslist \  
# \--conflicts=libuninameslist \  
# \--replaces=libuninameslist && \  
# cd .. && \  
# git clone git://git.sv.gnu.org/freetype/freetype2.git && \  
# cd freetype2 && \  
# ./autogen.sh && \  
# sed -e "/AUX.*.gxvalid/s@^# @@" \  
# -e "/AUX.*.otvalid/s@^# @@" \  
# -i modules.cfg && \  
# sed -r -e 's:.*(#.*SUBPIXEL.*) .*:\1:' \  
# -i include/freetype/config/ftoption.h && \  
# ./configure --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=freetype2 \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{4\\}//') \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=freetype2 \  
# \--conflicts=freetype2 \  
# \--replaces=freetype2 && \  
# cd .. && \  
# git clone git://anongit.freedesktop.org/fontconfig && \  
# cd fontconfig && \  
# ./autogen.sh && \  
# ./configure \  
# \--prefix=/usr \  
# \--sysconfdir=/etc \  
# \--localstatedir=/var \  
# \--disable-docs && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=fontconfig \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=fontconfig \  
# \--conflicts=fontconfig \  
# \--replaces=fontconfig && \  
# cd .. && \  
# git clone git://git.gnome.org/pango && \  
# cd pango && \  
# ./autogen.sh && \  
# ./configure \  
# \--prefix=/usr \  
# \--sysconfdir=/etc && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=pango \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=pango \  
# \--conflicts=pango \  
# \--replaces=pango && \  
# cd .. && \  
# git clone \--depth=1 git://anongit.freedesktop.org/poppler/poppler-data && \  
# cd poppler-data && \  
# sed -i -e 's:/usr/local:/usr:g' Makefile && \  
# printf "\n0.4.7\n\n" | checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=poppler-data \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{13\\}//') \  
# \--maintainer="Richard Yang" \  
# \--provides=poppler-data \  
# \--conflicts=poppler-data \  
# \--replaces=poppler-data && \  
# cd .. && \  
# git clone git://anongit.freedesktop.org/poppler/poppler && \  
# cd poppler && \  
# ./autogen.sh && \  
# ./configure \  
# \--prefix=/usr \  
# \--sysconfdir=/etc \  
# \--enable-build-type=release \  
# \--enable-cmyk \  
# \--enable-xpdf-headers && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=poppler \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{8\\}//') \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=poppler \  
# \--conflicts=poppler \  
# \--replaces=poppler && \  
# cd .. && \  
# git clone git://anongit.freedesktop.org/pixman && \  
# cd pixman && \  
# ./autogen.sh && \  
# ./configure --prefix=/usr && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=pixman \  
# \--pkgversion=$(git describe --tags --always | sed 's/^.\\{7\\}//') \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=pixman,libpixman-1-dev \  
# \--conflicts=pixman \  
# \--replaces=pixman,libpixman-1-dev && \  
# cd .. && \  
# git clone git://anongit.freedesktop.org/cairo && \  
# cd cairo && \  
# ./autogen.sh && \  
# auto-apt -y run ./configure \  
# \--prefix=/usr \  
# \--enable-tee && \  
# make && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=cairo \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--fstrans=no \  
# \--maintainer="Richard Yang" \  
# \--provides=cairo,libcairo2-dev \  
# \--conflicts=cairo \  
# \--replaces=cairo,libcairo2-dev && \  
# cd ..  
# git clone git://repo.or.cz/ttfautohint.git && \  
# cd fontforge && \  
# ./bootstrap && \  
# ./configure --prefix=/usr && \  
# make && \  
# checkinstall \  
# \--showinstall=no \  
# \--nodoc \  
# \--pkgname=fontforge \  
# \--pkgversion=$(git describe --tags --always) \  
# \--default \  
# \--maintainer="Richard Yang" \  
# \--provides=fontforge \  
# \--conflicts=fontforge \  
# \--replaces=fontforge && \  
# cd .. && \  
git clone git://github.com/coolwanglu/pdf2htmlEX && \  
cd pdf2htmlEX && \  
cmake . && \  
checkinstall \  
\--showinstall=no \  
\--nodoc \  
\--pkgname=pdf2htmlex \  
\--pkgversion=$(git describe --tags --always | sed 's/^.\\{1\\}//') \  
\--default \  
\--maintainer="Richard Yang" \  
\--provides=pdf2htmlex \  
\--conflicts=pdf2htmlex \  
\--replaces=pdf2htmlex && \  
cd ..  
# echo 'export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' >>
/root/.zshrc && \  
# echo 'export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' >>
/root/.bashrc && \  
# source /root/.zshrc && \  
# source /root/.bashrc  
COPY manifest /usr/local/share/pdf2htmlEX/  
  
VOLUME /pdf  
  
WORKDIR /pdf  
  
ENTRYPOINT ["pdf2htmlEX", "--split-pages=1", "--embed=cfijo", "--page-
filename=%04d.xhtml", "--hdpi=150", "--vdpi=150", "--space-as-offset=1", "--
optimize-text=1", "--correct-text-visibility=1"]  
CMD ["--help"]  
#Dockerfile  

