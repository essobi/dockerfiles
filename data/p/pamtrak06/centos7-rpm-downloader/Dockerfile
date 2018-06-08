FROM centos:centos7  
RUN yum -y update && yum -y install tree yum-utils  
RUN mkdir /scripts  
ADD *.sh /scripts/  
RUN chmod a+x /scripts/*.sh  
  
ENV RPM_PATH=/packages \  
PATH=$PATH:/scripts  
  
RUN mkdir $RPM_PATH  
WORKDIR $RPM_PATH  
  
# Path where rmp and their dependencies are downloaded  
VOLUME $RPM_PATH  
  
# Resolution mode  
ARG RESOLVE_MODE  
  
# Recursive mode  
ARG RECURSIVE_MODE  
ARG RECURSIVE_MAX_LEVEL=1  
ENV RECURSIVE_MAX_LEVEL=$RECURSIVE_MAX_LEVEL  
  
# Yum downloader options  
ARG YUMDOWNLOADER_OPTIONS=""  
ENV YUMDOWNLOADER_OPTIONS=$YUMDOWNLOADER_OPTIONS  
  
# Debug mode  
ARG TRACE_ONLY_MODE  
  
# List of packages in env. variable  
ARG RPM_LIST  
  
# List of packages in file  
ARG FILE_LIST  
# Item index of packages in file  
ARG RPM_FILE_ITEM_INDEX  
  
CMD [ "bash", "-c", "/scripts/docker-entrypoint.sh" ]  

