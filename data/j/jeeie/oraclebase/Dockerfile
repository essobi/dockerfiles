FROM centos:5.11  
  
MAINTAINER Jiang Ying (jy0000@gmail.com)  
  
ENV TEMP_INSTALL_PATH=/tmp  
  
ADD oracle.yumlist ${TEMP_INSTALL_PATH}/  
ADD install_rpms.sh ${TEMP_INSTALL_PATH}/  
  
############################  
## Update Base OS ##  
############################  
RUN \  
chmod +x ${TEMP_INSTALL_PATH}/install_rpms.sh && \  
cd ${TEMP_INSTALL_PATH} && \  
./install_rpms.sh  

