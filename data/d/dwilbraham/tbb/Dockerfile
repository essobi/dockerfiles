FROM gcc:4  
ENV TBB_VERSION 44_20160128  
ENV TBB_DOWNLOAD_URL
https://www.threadingbuildingblocks.org/sites/default/files/software_releases/linux/tbb${TBB_VERSION}oss_lin.tgz  
ENV TBB_INSTALL_DIR /opt  
  
RUN wget ${TBB_DOWNLOAD_URL} \  
&& tar -C ${TBB_INSTALL_DIR} -xf tbb${TBB_VERSION}oss_lin.tgz \  
&& rm tbb${TBB_VERSION}oss_lin.tgz  
  
RUN sed -i
"s%SUBSTITUTE_INSTALL_DIR_HERE%${TBB_INSTALL_DIR}/tbb${TBB_VERSION}oss%"
${TBB_INSTALL_DIR}/tbb${TBB_VERSION}oss/bin/tbbvars.*  
  
RUN echo "source ${TBB_INSTALL_DIR}/tbb${TBB_VERSION}oss/bin/tbbvars.sh
intel64" >> /etc/bash.bashrc  

