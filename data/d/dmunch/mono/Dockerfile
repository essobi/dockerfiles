FROM ubuntu:14.04  
#Get latest packaged version of Mono to bootstrap  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo
tee /etc/apt/sources.list.d/mono-xamarin.list  
  
RUN apt-get update && \  
apt-get install -y mono-devel mono-mcs libtool autoconf g++ gettext make git
&& \  
git clone https://github.com/dmunch/mono --branch openxml-fixes-4.2 --single-
branch && \  
cd mono && \  
./autogen.sh --prefix /opt/mono --with-ikvm-native=no && \  
make -j 4 && \  
make install && \  
#cleanup && \  
apt-get purge -y mono-devel mono-mcs libtool autoconf g++ gettext make && \  
apt-get autoremove -y && \  
cd .. && rm -rf mono && \  
#install pcl reference assemblies && \  
apt-get install -y wget unzip && \  
cd /root && \  
wget https://github.com/directhex/xamarin-referenceassemblies-
pcl/archive/master.zip && \  
unzip master.zip && \  
mkdir /opt/mono/lib/mono/xbuild-frameworks/.NETPortable/ && \  
cp -r /root/xamarin-referenceassemblies-pcl-master/*
/opt/mono/lib/mono/xbuild-frameworks/.NETPortable/ && \  
#cleanup && \  
rm -rf master.zip && \  
rm -rf xamarin-referenceassemblies-pcl-master && \  
apt-get clean  
  
#mono doesn't ship v4.5.2 libraries yet, just symlink (yeah, a little evil)  
RUN ln -s /opt/mono/lib/mono/xbuild-frameworks/.NETFramework/v4.5.1/
/opt/mono/lib/mono/xbuild-frameworks/.NETFramework/v4.5.2  
#set environement variables for custom mono path /opt/mono  
ENV MONO_PREFIX /opt/mono  
ENV GNOME_PREFIX /opt/gnome  
ENV DYLD_FALLBACK_LIBRARY_PATH $MONO_PREFIX/lib:$DYLD_LIBRARY_FALLBACK_PATH  
ENV LD_LIBRARY_PATH $MONO_PREFIX/lib:$LD_LIBRARY_PATH  
ENV C_INCLUDE_PATH $MONO_PREFIX/include:$GNOME_PREFIX/include  
ENV ACLOCAL_PATH $MONO_PREFIX/share/aclocal  
ENV PKG_CONFIG_PATH $MONO_PREFIX/lib/pkgconfig:$GNOME_PREFIX/lib/pkgconfig  
ENV PATH $MONO_PREFIX/bin:$PATH  
ENV PS1 "[mono] \w @ "  
  
RUN mozroots --import --sync  

