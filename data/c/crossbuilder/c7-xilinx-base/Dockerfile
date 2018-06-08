FROM crossbuilder/c7-gui-base:testing  
  
MAINTAINER crossbuilder  
  
LABEL Version 0.1  
  
RUN yum -y install xinetd gcc git subversion zlib-devel ncurses-devel openssl-
devel dos2unix \  
iproute gawk gnutls-devel net-tools tftp-server flex bison \  
libselinux1 bc unzip minicom screen \  
libstdc++.i686 glibc.i686 libgcc.i686 libgomp.i686 ncurses-libs.i686 zlib.i686
\  
fontconfig.i686 libXext.i686 libXrender.i686 glib2.i686 libpng12.i686
libSM.i686 \  
usbutils expect \  
python34 nc \  
wget \  
rdfind \  
bash-completion kdiff3 ; \  
yum clean all  
  
RUN sed -ie 's/disable.*= yes/disable = no/' /etc/xinetd.d/tftp  
  
EXPOSE 22  

