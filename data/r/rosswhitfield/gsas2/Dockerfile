FROM ubuntu:trusty  
MAINTAINER Ross Whitfield <whitfieldre@ornl.gov>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install subversion gfortran python-matplotlib python-scipy python-
numpy python-pil python-wxgtk2.8 python-opengl curl -y  
RUN mkdir /root/gsas2 && curl
https://subversion.xray.aps.anl.gov/pyGSAS/install/bootstrap.py >
/root/gsas2/bootstrap.py  
RUN /usr/bin/python /root/gsas2/bootstrap.py  
  
CMD ["/root/gsas2/GSASII.py"]  

