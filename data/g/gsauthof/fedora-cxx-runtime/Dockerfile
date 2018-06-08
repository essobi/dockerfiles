FROM fedora:27  
MAINTAINER Georg Sauthoff <mail@georg.so>  
  
# gcc is included because it provides gcov  
RUN dnf -y install \  
boost \  
findutils \  
gcc \  
glibc.i686 \  
lcov \  
libasan \  
liblsan \  
libtsan \  
libubsan \  
libxml2 \  
llvm \  
lua \  
luajit \  
openbox \  
procps-ng \  
qt5-qtbase \  
qt5-qtsvg \  
xfwm4 \  
xorg-x11-server-Xvfb \  
&& dnf clean all  
  
# openbox is more leightweight than xfwm4,  
# but xfwm4 pulls in some gtk libraries in which are needed  
# when running with DESKTOP_SESSION=gnome  
# Also, xfwm4 seems to be more reliable regarding  
# QApplicateion::focusWidget() || activeWindow()  
# mount points for mapping source code and  
# build directories  
RUN mkdir /srv/{src,build}  
  
# on fedora should reliable get uid/gid 1000  
RUN useradd -m compile-user  
RUN systemd-machine-id-setup  
COPY start_xvfb.sh /usr/local/bin  
USER compile-user  
WORKDIR /home/compile-user  
ENV DISPLAY :1  
ENTRYPOINT [ "/usr/local/bin/start_xvfb.sh" ]  

