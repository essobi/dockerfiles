FROM fgagnaire/centos73-gui:latest  
  
  
MAINTAINER francis gagnaire  
USER root  
  
  
# needed for building wireshark  
RUN yum install -y autoconf automake libtool byacc flex qt-devel gtk3-devel \  
&& yum install -y libpcap-devel lua-devel c-ares-devel qt5-qtbase-devel \  
&& yum install -y qt5-qtmultimedia-devel desktop-file-utils qt5-qttools-devel
\  
&& yum install -y libgcrypt-devel \  
&& yum clean all  
  
# be able to run wireshark within docker. (because of Qt)  
ENV QT_GRAPHICSSYSTEM "native"  
  
CMD /bin/bash  
  

