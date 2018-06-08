FROM ubuntu:trusty  
MAINTAINER Ross Whitfield <whitfieldre@ornl.gov>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install software-properties-common gdebi wget -y  
RUN apt-add-repository ppa:mantid/mantid && apt-get update  
RUN wget
http://sourceforge.net/projects/mantid/files/3.5/mantid_3.5.0-1_amd64.deb/download
-O /root/mantid_3.5.0-1_amd64.deb  
RUN gdebi --n /root/mantid_3.5.0-1_amd64.deb  
  
CMD ["/opt/Mantid/bin/MantidPlot"]  

