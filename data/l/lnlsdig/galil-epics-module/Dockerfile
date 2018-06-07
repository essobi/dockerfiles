FROM lnls/epics-dist:base-3.15-debian-9  
  
ENV MODULE_OWNER motorapp  
ENV MODULE_REPO Galil-3-0  
ENV VERSION 3-6  
ENV COMMIT V${VERSION}  
  
RUN git clone https://github.com/${MODULE_OWNER}/${MODULE_REPO}.git
/opt/epics/${MODULE_REPO} && \  
cd /opt/epics/${MODULE_REPO} && \  
git checkout ${COMMIT} && \  
cd ${VERSION} && \  
sed -i -e 's|^EPICS_BASE=.*$|EPICS_BASE=/opt/epics/base|' config/GALILRELEASE
&& \  
sed -i -e 's|^SUPPORT=.*$|SUPPORT=/opt/epics/synApps-lnls-R0-0-2/support|'
config/GALILRELEASE && \  
sed -i -e 's|^AUTOSAVE=.*$|AUTOSAVE=$(SUPPORT)/autosave-R5-9|'
config/GALILRELEASE && \  
sed -i -e 's|^SNCSEQ=.*$|SNCSEQ=$(SUPPORT)/seq-2-2-6|' config/GALILRELEASE &&
\  
sed -i -e 's|^SSCAN=.*$|SSCAN=$(SUPPORT)/sscan-R2-11-1|' config/GALILRELEASE
&& \  
sed -i -e 's|^CALC=.*$|CALC=$(SUPPORT)/calc-R3-7|' config/GALILRELEASE && \  
sed -i -e 's|^ASYN=.*$|ASYN=$(SUPPORT)/asyn-R4-33|' config/GALILRELEASE && \  
sed -i -e 's|^BUSY=.*$|BUSY=$(SUPPORT)/busy-R1-7|' config/GALILRELEASE && \  
sed -i -e 's|^MOTOR=.*$|MOTOR=$(SUPPORT)/motor-R6-10|' config/GALILRELEASE &&
\  
sed -i -e 's|^IPAC=.*$|IPAC=$(SUPPORT)/ipac-2-15|' config/GALILRELEASE && \  
sed -i -e 's|^GALIL=.*$|#GALIL=|' config/GALILRELEASE && \  
cd GalilSup && \  
make  

