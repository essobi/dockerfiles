FROM cnlspacebel/landcover:0.2  
  
MAINTAINER Forestry TEP  
  
###########################  
# Download and install SNAP  
ENV SNAP_MAJ_VER='5'\  
SNAP_MIN_VER='0'\  
SNAP_POINT_VER='0'  
  
ENV
SNAP_BASE_URL="http://step.esa.int/downloads/${SNAP_MAJ_VER}.${SNAP_MIN_VER}/installers"\  
SNAP_INSTALLER="esa-snap_sentinel_unix_${SNAP_MAJ_VER}_${SNAP_MIN_VER}.sh"  
  
LABEL snap.version="${SNAP_MAJ_VER}.${SNAP_MIN_VER}.${SNAP_POINT_VER}"  
  
##########################  
# Download and install OTB  
ENV OTB_MAJ_VER='5'\  
OTB_MIN_VER='8'\  
OTB_POINT_VER='0'  
  
ENV OTB_BASE_URL="https://www.orfeo-toolbox.org/packages"\  
OTB_ALT_URL="https://www.orfeo-toolbox.org/packages/archives/OTB"\  
OTB_INSTALLER="OTB-${OTB_MAJ_VER}.${OTB_MIN_VER}.${OTB_POINT_VER}-Linux64.run"  
  
LABEL otb.version="${OTB_MAJ_VER}.${OTB_MIN_VER}.${OTB_POINT_VER}"  
  
  
ENV
PATH=/opt/OTB-${OTB_MAJ_VER}.${OTB_MIN_VER}.${OTB_POINT_VER}-Linux64/bin:/opt/snap/bin:${PATH}  
  
COPY * /home/worker/processor/  
RUN ["chmod", "-R", "a+wr", "/home/worker/processor"]  
RUN ["chmod", "a+x", "/home/worker/processor/workflow.sh"]  
ENTRYPOINT ["/home/worker/processor/workflow.sh"]  

