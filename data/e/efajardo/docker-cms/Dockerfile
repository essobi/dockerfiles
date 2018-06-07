FROM opensciencegrid/tensorflow-gpu  
  
LABEL name="CMS tensorflow-gpu"  
LABEL build-date="20180122"  
LABEL maintainer="Edgar Fakardo"  
  
# Required  
# --------  
#  
# Experimental  
#  
# Various directories needed for bind mounts (as overlayfs is not available on
RHEL6)  
RUN mkdir -p /hdfs \  
/mnt/hadoop \  
/hadoop \  
/cms \  
/etc/cvmfs/SITECONF \  
/lfs_roots  
  

