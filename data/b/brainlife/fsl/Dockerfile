FROM ubuntu:xenial  
MAINTAINER Soichi Hayashi <hayashis@iu.edu>  
  
RUN apt-get update && apt-get install -y wget jq vim  
  
#install neurodebian  
RUN wget -O- http://neuro.debian.net/lists/xenial.us-tn.full | tee
/etc/apt/sources.list.d/neurodebian.sources.list  
RUN apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80
0xA5D32F012649A5A9  
  
#install fsl  
RUN apt-get update && apt-get install -y fsl  
  
ENV FSLDIR=/usr/share/fsl/5.0  
ENV PATH=$PATH:$FSLDIR/bin  
ENV LD_LIBRARY_PATH=/usr/lib/fsl/5.0:/usr/share/fsl/5.0/bin  
  
#simulate . ${FSLDIR}/etc/fslconf/fsl.sh  
ENV FSLBROWSER=/etc/alternatives/x-www-browser  
ENV FSLCLUSTER_MAILOPTS=n  
ENV FSLLOCKDIR=  
ENV FSLMACHINELIST=  
ENV FSLMULTIFILEQUIT=TRUE  
ENV FSLOUTPUTTYPE=NIFTI_GZ  
ENV FSLREMOTECALL=  
ENV FSLTCLSH=/usr/bin/tclsh  
ENV FSLWISH=/usr/bin/wish  
ENV POSSUMDIR=/usr/share/fsl/5.0  
#make it work under singularity  
RUN ldconfig && mkdir -p /N/u /N/home /N/dc2 /N/soft  
  
#https://wiki.ubuntu.com/DashAsBinSh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  

