############################################################  
# Dockerfile to run the Folding@home Client  
############################################################  
  
FROM alpine:latest  
MAINTAINER Carlos Xavier Hernández <cxh@stanford.edu>  
  
# Set Environment Variables  
ENV BUILD_ROOT=$HOME/deps  
ENV CBANG_HOME=$BUILD_ROOT/cbang LIBFAH_HOME=$BUILD_ROOT/libfah
FAH_GROMACS_HOME=$BUILD_ROOT/fah-gromacs FAH_VIEWER_HOME=$BUILD_ROOT/fah-
viewer FAH_WEB_CLIENT_HOME=$BUILD_ROOT/fah-web-client
FAH_CLIENT_HOME=$BUILD_ROOT/fah-client
FAH_CLIENT_VERSION_HOME=$BUILD_ROOT/fah-client-version
BOOST_SOURCE=$BUILD_ROOT/boost_1_60_0 CONFIG=/config.xml  
  
COPY repositories /etc/apk/repositories  
COPY oauth.txt /oauth.txt  
COPY queue.h /usr/include/sys/queue.h  
  
RUN apk upgrade --update-cache --available && \  
apk add -U --allow-untrusted scons git gcc make g++ \  
mariadb-dev wget cmake bzip2-dev build-base \  
freetype-dev zlib-dev expat-dev libxml2-dev \  
freeglut-dev pkgconf tar sqlite-libs libevent-dev \  
valgrind-dev libre2-dev@edge && \  
mkdir $BUILD_ROOT && cd $BUILD_ROOT && \  
wget
http://sourceforge.net/projects/boost/files/boost/1.60.0/boost_1_60_0.tar.bz2/download
-O $BUILD_ROOT/boost_160.tar.bz2 && \  
tar --bzip2 -xf $BUILD_ROOT/boost_160.tar.bz2 && \  
rm $BUILD_ROOT/boost_160.tar.bz2 && cd $BOOST_SOURCE && \  
./bootstrap.sh --prefix=$BOOST_SOURCE/build --with-
libraries=iostreams,system,regex && \  
./b2 install -j4 && \  
GITHUB_OAUTH_TOKEN=`cat /oauth.txt` && \  
GITHUB=https://$GITHUB_OAUTH_TOKEN:x-oauth-basic@github.com && \  
rm /oauth.txt && cd $BUILD_ROOT && \  
git clone $GITHUB/cxhernandez/cbang.git && \  
git clone $GITHUB/FoldingAtHome/libfah.git && \  
git clone $GITHUB/FoldingAtHome/fah-gromacs.git && \  
git clone $GITHUB/FoldingAtHome/fah-client-version.git && \  
git clone $GITHUB/FoldingAtHome/fah-viewer.git && \  
git clone $GITHUB/FoldingAtHome/fah-web-client.git && \  
git clone $GITHUB/FoldingAtHome/fah-client.git && \  
cd $CBANG_HOME && git checkout alpine && \  
cd $LIBFAH_HOME && git checkout 1.0 && \  
scons -C $CBANG_HOME -j4 && \  
scons -C $LIBFAH_HOME -j4 && \  
scons -C $FAH_GROMACS_HOME fah=1 -j4 && \  
scons -C $FAH_VIEWER_HOME -j4 && \  
scons -C $FAH_WEB_CLIENT_HOME -j4 && \  
scons -C $FAH_CLIENT_HOME -j4 && \  
ln -s $FAH_CLIENT_HOME/FAHClient /usr/local/bin/FAHClient && \  
ln -s $FAH_CLIENT_HOME/FAHClient.init.d /etc/FAHClient.init.d && \  
rm -rf $CBANG_HOME \  
$LIBFAH_HOME \  
$FAH_GROMACS_HOME \  
$FAH_VIEWER_HOME \  
$FAH_WEB_CLIENT_HOME \  
$BOOST_SOURCE \  
$FAH_CLIENT_VERSION_HOME && \  
ls $FAH_CLIENT_HOME | grep -v FAH* | xargs rm -rf && \  
apk del scons git gcc make g++ tar \  
wget cmake build-base valgrind-dev \  
libxml2-dev mariadb-dev freeglut-dev \  
libre2-dev libevent-dev && \  
apk add libstdc++ libgcc freetype-dev glu freeglut bzip2-dev  
  
# Run FAHClient  
CMD echo "<config>" > config.xml && \  
echo "<user value='$USERNAME'/>" >> config.xml && \  
echo "<team value='$TEAM'/>" >> config.xml && \  
echo "<passkey value='$PASSKEY'/>" >> config.xml && \  
echo "<smp value='$SMP'/>" >> config.xml && \  
echo "<gpu value='$GPU'/>" >> config.xml && \  
echo "</config>" >> config.xml && \  
FAHClient $CONFIG  

