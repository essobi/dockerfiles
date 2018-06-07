FROM lnls/epics-dist:base-3.15-debian-9  
ENV EPICS_REPO inj-efficiency-epics-ioc  
ENV BOOT_DIR iocInjEfficiency  
ENV COMMIT v1.0.0  
RUN git clone https://github.com/lnls-dig/${EPICS_REPO}.git
/opt/epics/${EPICS_REPO} && \  
cd /opt/epics/${EPICS_REPO} && \  
git checkout ${COMMIT} && \  
sed -i -e 's|^EPICS_BASE=.*$|EPICS_BASE=/opt/epics/base|' configure/RELEASE &&
\  
sed -i -e 's|^SUPPORT=.*$|SUPPORT=/opt/epics/synApps-lnls-R0-0-2/support|'
configure/RELEASE && \  
sed -i -e 's|^SNCSEQ=.*$|SNCSEQ=$(SUPPORT)/seq-2-2-6|' configure/RELEASE && \  
sed -i -e 's|^CALC=.*$|CALC=$(SUPPORT)/calc-R3-7|' configure/RELEASE && \  
sed -i -e 's|^ASYN=.*$|ASYN=$(SUPPORT)/asyn-R4-33|' configure/RELEASE && \  
sed -i -e 's|^AUTOSAVE=.*$|AUTOSAVE=$(SUPPORT)/autosave-R5-9|'
configure/RELEASE && \  
make && \  
make install && \  
make clean  
  
# Source environment variables until we figure it out  
# where to put system-wide env-vars on docker-debian  
RUN . /root/.bashrc  
  
WORKDIR /opt/epics/startup/ioc/${EPICS_REPO}/iocBoot/${BOOT_DIR}  
  
ENTRYPOINT ["./runProcServ.sh"]  

