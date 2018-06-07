FROM lnlsdig/galil-epics-module:V3-6-base-3.15-debian-9  
ENV IOC_REPO galil-dmc30017-epics-ioc  
ENV BOOT_DIR iocGalilDmc30017  
ENV COMMIT v0.7.0  
RUN git clone https://github.com/lnls-dig/${IOC_REPO}.git
/opt/epics/${IOC_REPO} && \  
cd /opt/epics/${IOC_REPO} && \  
git checkout ${COMMIT} && \  
echo 'EPICS_BASE=/opt/epics/base' > configure/RELEASE.local && \  
echo 'SUPPORT=/opt/epics/synApps-lnls-R0-0-2/support' >>
configure/RELEASE.local && \  
echo 'AUTOSAVE=$(SUPPORT)/autosave-R5-9' >> configure/RELEASE.local && \  
echo 'SNCSEQ=$(SUPPORT)/seq-2-2-6' >> configure/RELEASE.local && \  
echo 'SSCAN=$(SUPPORT)/sscan-R2-11-1' >> configure/RELEASE.local && \  
echo 'CALC=$(SUPPORT)/calc-R3-7' >> configure/RELEASE.local && \  
echo 'ASYN=$(SUPPORT)/asyn-R4-33' >> configure/RELEASE.local && \  
echo 'BUSY=$(SUPPORT)/busy-R1-7' >> configure/RELEASE.local && \  
echo 'MOTOR=$(SUPPORT)/motor-R6-10' >> configure/RELEASE.local && \  
echo 'IPAC=$(SUPPORT)/ipac-2-15' >> configure/RELEASE.local && \  
echo 'GALIL=/opt/epics/Galil-3-0/3-6' >> configure/RELEASE.local && \  
make && \  
make install  
  
# Source environment variables until we figure it out  
# where to put system-wide env-vars on docker-debian  
RUN . /root/.bashrc  
  
WORKDIR /opt/epics/startup/ioc/${IOC_REPO}/iocBoot/${BOOT_DIR}  
  
ENTRYPOINT ["./runProcServ.sh"]  

