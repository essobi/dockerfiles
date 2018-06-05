FROM caffeinatedexpert/docker-oracle7-slim-java8:latest  
  
ENV COH_INSTALLER coherence-12.2.1.0.3.1.jar  
  
RUN mkdir /u01 && chmod a+xr /u01 && \  
useradd -b /u01 -m -s /bin/bash oracle && \  
echo oracle:oracle | chpasswd && \  
chown oracle /u01 && \  
mkdir /home/oracle && \  
chown oracle /home/oracle  
  
RUN curl -o /u01/$COH_INSTALLER https://storage.googleapis.com/gcp-gdis-
tools/public/downloads/$COH_INSTALLER  
  
#COPY coh.rsp /u01/  
#COPY oraInst.loc /u01/oraInst.loc  
RUN chown oracle /u01/$COH_INSTALLER  
RUN ls -l /u01/$COH_INSTALLER  
# && chown oracle /u01/coh.rsp \  
# && chown oracle /u01/oraInst.loc  
ENV COHERENCE_HOME=/u01/app/oracle/coherence/coherence  
  
USER oracle  
  
RUN curl -o /u01/cache-server.sh https://storage.googleapis.com/gcp-gdis-
tools/public/downloads/cache-server.sh \  
&& curl -o /u01/coherence.sh https://storage.googleapis.com/gcp-gdis-
tools/public/downloads/coherence.sh \  
&& curl -o /u01/tangosol-coherence-override.xml
https://storage.googleapis.com/gcp-gdis-tools/public/downloads/tangosol-
coherence-override.xml \  
&& chmod +x /u01/*.sh  
  
#RUN java -jar /u01/$COH_INSTALLER -silent -force -responseFile /u01/coh.rsp
-invPtrLoc /u01/oraInst.loc -jreLoc $JAVA_HOME \  
# && rm /u01/$COH_INSTALLER \  
# && rm /u01/coh.rsp \  
# && rm /u01/oraInst.loc \  
# && rm -rf /tmp/OraInstall*

