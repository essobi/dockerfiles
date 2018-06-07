FROM dynainstrumentsoss/ptxdist-arm-v5te:2014-04  
MAINTAINER Johannes Lode, DYNA Instruments GmbH Hamburg,
http://www.dynainstruments.com  
  
# add some prefetched distfiles, which are hard to get or lost on the net  
ADD cached-distfiles.tar /home/ptxdist/distfiles/  
  
# add the BSP  
ADD DYNA-ECO-G45_BSP_linux-3.14.tar /home/ptxdist/  
  
WORKDIR /home/ptxdist/BSP-3.14  
USER ptxdist  
VOLUME /tftpboot  
CMD ["/bin/bash", "-il"]  

