FROM thewtex/centos-build:latest  
  
#RUN apt-get update  
#RUN apt-get install --yes curl zip unzip  
  
ADD setup_slicer.sh /usr/src/setup_slicer.sh  
RUN /usr/src/setup_slicer.sh  
  
ADD setup_dcm2niix.sh /usr/src/setup_dcm2niix.sh  
RUN /usr/src/setup_dcm2niix.sh  
#RUN setup_dcm2niix.sh  
#RUN mkdir -p /usr/dcm2niix  
#RUN wget
https://github.com/rordenlab/dcm2niix/releases/download/v1.0.20171215/dcm2niix_3-Jan-2018_lnx.zip
-o /usr/dcm2niix/dcm2niix.zip  
#RUN cd /usr/dcm2niix && unzip dcm2niix.zip && rm dcm2niix.zip  

