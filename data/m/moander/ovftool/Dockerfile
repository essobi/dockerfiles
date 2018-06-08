FROM buildpack-deps:curl  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends nano \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV OVFTOOL_VERSION 4.1.0-2459827  
RUN OVFTOOL_INSTALLER=vmware-ovftool-${OVFTOOL_VERSION}-lin.x86_64.bundle \  
&& wget -q
https://storage.googleapis.com/mortarchive/pub/ovftool/${OVFTOOL_INSTALLER} \  
&& wget -q
https://storage.googleapis.com/mortarchive/pub/ovftool/${OVFTOOL_INSTALLER}.sha256
\  
&& sha256sum -c ${OVFTOOL_INSTALLER}.sha256 \  
&& sh ${OVFTOOL_INSTALLER} -p /usr/local \--eulas-agreed --required \  
&& rm -f ${OVFTOOL_INSTALLER}*  
  
CMD [ "ovftool", "--help" ]  

