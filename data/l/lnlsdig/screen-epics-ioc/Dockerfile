FROM lnls/epics-dist:debian-9.2  
ENV IOC_REPO screen-epics-ioc  
ENV BOOT_DIR iocScreen  
ENV COMMIT v0.2.0  
RUN git clone https://github.com/lnls-dig/${IOC_REPO}.git
/opt/epics/${IOC_REPO} && \  
cd /opt/epics/${IOC_REPO} && \  
git checkout ${COMMIT} && \  
echo 'EPICS_BASE=/opt/epics/base' > configure/RELEASE.local && \  
echo 'SUPPORT=/opt/epics/synApps_5_8/support' >> configure/RELEASE.local && \  
echo 'AUTOSAVE=$(SUPPORT)/autosave-5-6-1' >> configure/RELEASE.local && \  
echo 'SNCSEQ=$(SUPPORT)/seq-2-2-1' >> configure/RELEASE.local && \  
echo 'CALC=$(SUPPORT)/calc-3-4-2-1' >> configure/RELEASE.local && \  
echo 'BUSY=$(SUPPORT)/busy-1-6-1' >> configure/RELEASE.local && \  
make && \  
make install  
  
# Source environment variables until we figure it out  
# where to put system-wide env-vars on docker-debian  
RUN . /root/.bashrc  
  
WORKDIR /opt/epics/startup/ioc/${IOC_REPO}/iocBoot/${BOOT_DIR}  
  
ENTRYPOINT ["./runProcServ.sh"]  

