FROM centos:centos7  
MAINTAINER Jeremie Lesage <jeremie.lesage@gmail.com>  
  
  
ENV LIBREOFFICE_VERSION="5.4.3" \  
LIBREOFFICE_VERSION_MINOR="5.4.3.2"  
ENV
LIBREOFFICE_DOWNLOAD_MIRROR="http://download.documentfoundation.org/libreoffice/stable"
\  
HOST="0.0.0.0" \  
PORT="8100" \  
LIBREOFFICE_HOME="/opt/libreoffice5.4" \  
LIBREOFFICE_RPM_TGZ="LibreOffice_${LIBREOFFICE_VERSION}_Linux_x86-64_rpm.tar.gz"
\  
LIBREOFFICE_RPM_DIR="LibreOffice_${LIBREOFFICE_VERSION_MINOR}_Linux_x86-64_rpm"
\  
PATH=/opt/libreoffice/program:$PATH  
  
RUN mkdir /opt/libreoffice5.4  
  
RUN echo "curl -L
${LIBREOFFICE_DOWNLOAD_MIRROR}/${LIBREOFFICE_VERSION}/rpm/x86_64/${LIBREOFFICE_RPM_TGZ}
| tar xz " \  
&& curl -L
${LIBREOFFICE_DOWNLOAD_MIRROR}/${LIBREOFFICE_VERSION}/rpm/x86_64/${LIBREOFFICE_RPM_TGZ}
| tar xz \  
&& yum install -y fontconfig libSM libICE libXrender libXext cups-libs cairo \  
xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi ghostscript-fonts \  
gnu-free-sans-fonts gnu-free-serif-fonts liberation-serif-fonts \  
liberation-sans-fonts liberation-mono-fonts freetype open-sans-fonts \  
&& yum clean all \  
&& yum install -y \  
${LIBREOFFICE_RPM_DIR}/RPMS/libreoffice5.4-*.rpm \  
${LIBREOFFICE_RPM_DIR}/RPMS/libobasis5.4-*.rpm \  
&& yum clean all \  
&& rm -rf ${LIBREOFFICE_RPM_DIR} ${LIBREOFFICE_RPM_TGZ} \  
&& useradd -ms /bin/bash libreoffice \  
&& chown -R libreoffice:libreoffice ${LIBREOFFICE_HOME} \  
&& ln -s ${LIBREOFFICE_HOME} /opt/libreoffice  
  
WORKDIR /opt/libreoffice  
  
EXPOSE ${PORT}  
  
#COPY assets/sofficerc /etc/libreoffice/sofficerc  
COPY assets/entrypoint.sh /opt/libreoffice/  
RUN chmod +x /opt/libreoffice/entrypoint.sh  
  
ENTRYPOINT ["/opt/libreoffice/entrypoint.sh"]  
CMD ["run"]

