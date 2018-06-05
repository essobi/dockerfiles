FROM lnls/epics-dist:debian-9.2  
ENV IOC_REPO agilent33521a-epics-ioc  
ENV BOOT_DIR iocagilent33521a  
ENV COMMIT v1.0.0  
RUN git clone https://github.com/lnls-dig/${IOC_REPO}.git
/opt/epics/${IOC_REPO} && \  
cd /opt/epics/${IOC_REPO} && \  
git checkout ${COMMIT} && \  
sed -i -e 's|^EPICS_BASE=.*$|EPICS_BASE=/opt/epics/base|' configure/RELEASE &&
\  
sed -i -e 's|^SUPPORT=.*$|SUPPORT=/opt/epics/synApps_5_8/support|'
configure/RELEASE && \  
sed -i -e 's|^STREAM=.*$|STREAM=/opt/epics/stream|' configure/RELEASE && \  
sed -i -e 's|^AUTOSAVE=.*$|AUTOSAVE=$(SUPPORT)/autosave-5-6-1|'
configure/RELEASE && \  
make && \  
make install && \  
make clean  
  
# Source environment variables until we figure it out  
# where to put system-wide env-vars on docker-debian  
RUN . /root/.bashrc  
  
WORKDIR /opt/epics/startup/ioc/${IOC_REPO}/iocBoot/${BOOT_DIR}  
  
ENTRYPOINT ["./runProcServ.sh"]  

