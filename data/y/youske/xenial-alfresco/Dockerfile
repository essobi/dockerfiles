# ubuntu xenial with alfresco  
FROM youske/ubuntu-stdmachine:base  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
ENV ALFRESCO_VERSION=201605 \  
ALFRESCO_BUILD=00010 \  
ALFRESCO_BASE=/alfresco-community \  
LANGUAGE=ja_JP.UTF-8 \  
SHARE_PORT=8080 \  
FTP_PORT=21 \  
ADMIN_PASSWORD=admin  
  
#ENV DATA_DIR=${ALFRESCO_BASE}/alf_data  
RUN PACKAGE="fontconfig libice6 libsm6 libxt6 libxrender1 libfontconfig1
libglu1-mesa libdbus-glib-1-2 libcups2 libxinerama1 xvfb imagemagick
ghostscript xfonts-base" && \  
apt-get update && apt-get -y -q upgrade && \  
apt-get install -y -q wget language-pack-ja ${PACKAGE}  
  
RUN
DOWNLOAD_URL=http://dl.alfresco.com/release/community/${ALFRESCO_VERSION}-build-${ALFRESCO_BUILD}/alfresco-
community-installer-${ALFRESCO_VERSION}-linux-x64.bin && \  
wget -q ${DOWNLOAD_URL} -O /tmp/alfresco-community.bin && \  
chmod +x /tmp/alfresco-community.bin && /tmp/alfresco-community.bin --mode
text --installer-language en \  
  
\--prefix ${ALFRESCO_BASE} \  
\--postgres_port 5432 \  
\--tomcat_server_port ${SHARE_PORT} \  
\--tomcat_server_shutdown_port 8005 \  
\--tomcat_server_ssl_port 8443 \  
\--tomcat_server_ajp_port 8009 \  
\--libreoffice_port 8100 \  
\--alfresco_ftp_port ${FTP_PORT} \  
\--alfresco_admin_password ${ADMIN_PASSWORD}  
  
# amps  
RUN ALFRESCO_AMPS=${ALFRESCO_BASE}/amps && \  
ALFRESCO_AMPSSHARE=${ALFRESCO_BASE}/amps_share && \  
ALFRESCO_LIBREOFFICE=${ALFRESCO_BASE}/libreoffice && \  
wget -qP ${ALFRESCO_AMPS} https://github.com/share-extras/js-
console/releases/download/v0.6.0-rc1/javascript-console-repo-0.6.0.amp && \  
wget -qP ${ALFRESCO_AMPS} https://github.com/Alfresco/alfresco-support-
tools/releases/download/1.10/support-tools-1.10.amp && \  
wget -qP ${ALFRESCO_AMPS} https://github.com/ntmcminn/alfresco-pdf-
toolkit/releases/download/1.3-Beta3/pdf-toolkit-repo.amp && \  
wget -qP ${ALFRESCO_AMPSSHARE} https://github.com/ntmcminn/alfresco-pdf-
toolkit/releases/download/1.3-Beta3/pdf-toolkit-share.amp && \  
wget -qP ${ALFRESCO_AMPSSHARE} https://github.com/teqnology/alfresco-header-
share/blob/master/target/alfresco-header-share.amp?raw=true && \  
# wget -qP ${ALFRESCO_AMPSSHARE}
http://www.form4.de/fileadmin/user_upload/Pix/Leistungen/alfresco/extensions/form4.alfresco.htmlwebpreviewer-1.0.0.amp
&& \  
${ALFRESCO_BASE}/bin/apply_amps.sh && \  
ln -s -f ${ALFRESCO_LIBREOFFICE}/scripts/libreoffice_ctl.sh
${ALFRESCO_LIBREOFFICE}/scripts/ctl.sh  
  
ENV HEAPSIZE=1024M \  
MEMSIZE=3096M  
  
COPY scripts/ /alfresco_scripts  
COPY setenv.sh.tmpl ${ALFRESCO_BASE}/tomcat/bin  
COPY enable.d/ /tmp  
RUN cd ${ALFRESCO_BASE}/tomcat/shared/classes/ && \  
echo "\n" >> alfresco-global.properties && \  
cat /tmp/cifs >> alfresco-global.properties && \  
cat /tmp/ftp >> alfresco-global.properties && \  
cat /tmp/rmi >> alfresco-global.properties  
  
# remove downloadfile  
RUN apt-get autoremove && apt-get autoclean && rm -rf /tmp/*  
  
EXPOSE ${FTP_PORT} ${SHARE_PORT} 5432 8005 8100 8443 56000-56009  
WORKDIR /  
ENTRYPOINT ["render","/alfresco-community/tomcat/bin/setenv.sh","--","/init"]  
CMD ["/bin/bash","/alfresco_scripts/alfresco_run.sh"]  

