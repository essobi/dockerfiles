FROM java:8-jre  
MAINTAINER Mateusz Małek <mmalek@iisg.agh.edu.pl>  
  
ENV LCSRV_HOME /opt/jetbrains/lcsrv/home  
ENV LCSRV_INSTALL /opt/jetbrains/lcsrv/install  
  
RUN cd /tmp && \  
mkdir -p "${LCSRV_INSTALL}" && \  
wget https://download.jetbrains.com/lcsrv/license-server-installer.zip && \  
unzip license-server-installer.zip -d "${LCSRV_INSTALL}" && \  
rm license-server-installer.zip && \  
useradd --home-dir "${LCSRV_HOME}" \--shell /bin/bash --create-home lcsrv && \  
chmod -R o+r "${LCSRV_INSTALL}" && \  
mv "${LCSRV_INSTALL}/conf" "${LCSRV_HOME}/" && \  
echo -n "${LCSRV_HOME}/conf" > "${LCSRV_INSTALL}/service.conf.location"  
  
VOLUME $LCSRV_HOME  
  
EXPOSE 1111  
ADD ./entrypoint.sh /entrypoint.sh  
  
WORKDIR $LCSRV_HOME  
USER lcsrv:lcsrv  
  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  

