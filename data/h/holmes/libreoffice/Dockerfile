FROM holmes/java:1.7.0_71  
MAINTAINER Holmes Team <holmes@holmesdoc.com>  
  
#Libreoffice instalation sometimes uses 4.3 as version and sometimes uses
4.3.4 as version  
ENV LIBREOFFICE_VERSION_MAJOR 4.3  
ENV LIBREOFFICE_VERSION_MINOR 4  
RUN yum install -y tar mesa-libGLU  
  
RUN DIR=$(mktemp -d) \  
&& cd ${DIR} \  
&& curl -L -Os
http://mirror.clarkson.edu/tdf/libreoffice/stable/${LIBREOFFICE_VERSION_MAJOR}.${LIBREOFFICE_VERSION_MINOR}/rpm/x86_64/LibreOffice_${LIBREOFFICE_VERSION_MAJOR}.${LIBREOFFICE_VERSION_MINOR}_Linux_x86-64_rpm.tar.gz
\  
&& tar xf
LibreOffice_${LIBREOFFICE_VERSION_MAJOR}.${LIBREOFFICE_VERSION_MINOR}_Linux_x86-64_rpm.tar.gz
\  
&& cd
LibreOffice_${LIBREOFFICE_VERSION_MAJOR}.${LIBREOFFICE_VERSION_MINOR}.1_Linux_x86-64_rpm
\  
&& cd RPMS \  
&& yum install -y *.rpm \  
&& ln -s /opt/libreoffice${LIBREOFFICE_VERSION_MAJOR}/program/soffice
/usr/bin/soffice \  
&& rm -rf ${DIR}  
  
ENTRYPOINT ["/usr/bin/soffice"]  
CMD ["--version"]

