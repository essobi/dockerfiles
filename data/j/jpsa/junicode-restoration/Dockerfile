FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y fontforge python-fontforge
ttfautohint unzip curl make python-pip lib32z1 libc6-i386  
  
RUN pip install -U fonttools  
# RUN curl
http://download.macromedia.com/pub/developer/opentype/FDK.2.5.65322/FDK-25-LINUX.b65322.zip
> FDK-25-LINUX.b65322.zip  
RUN curl
http://download.macromedia.com/pub/developer/opentype/FDK.2.5.65781/FDK.2.5.65781-LINUX.zip
> /FDK.zip  
  
RUN unzip /FDK.zip  
RUN /FDK/FinishInstallLinux  
  
ENV PATH /root/bin/FDK/Tools/linux:$PATH  
ENV FDK_EXE /root/bin/FDK/Tools/linux  
  
WORKDIR /font  
  
CMD make -f Makefile.ff  

