FROM debian:jessie  
  
MAINTAINER NSLS-II <https://nsls-ii.github.io>  
  
USER root  
  
# Install and start mongo  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key 7F0CEB10  
  
RUN apt-get update  
# Install the EPICS stack  
RUN apt-get install -yq wget  
  
RUN wget --quiet http://epics.nsls2.bnl.gov/debian/repo-key.pub -O - | apt-key
add -  
RUN echo "deb http://epics.nsls2.bnl.gov/debian/ jessie/staging main contrib"
| tee /etc/apt/sources.list.d/nsls2.list  
#RUN echo "deb http://ftp.us.debian.org/debian/ jessie non-free" | tee
/etc/apt/sources.list.d/non-free.list  
RUN apt-get update  
RUN apt-get install -yq build-essential git epics-dev epics-synapps-dev epics-
iocstats-dev  
RUN apt-get install -yq procserv telnet sysv-rc-softioc  
# get areadetector dependencies  
RUN apt-get install -yq libhdf5-dev libx11-dev libxext-dev libxml2-dev
libpng12-dev libbz2-dev libfreetype6-dev  
  
# pip install things not yet on lightsource2 channel.  
RUN apt-get install -yq python3 python3-pip python3-numpy  
# dependency dragged in from (at least) ophyd.commands  
RUN pip3 install https://github.com/pyepics/pyepics/zipball/master#egg=pyepics  
  
# clone and build EPICS device simulation code  
RUN mkdir /epics && mkdir /epics/iocs  
RUN mkdir /epics/src  
RUN git clone https://github.com/klauer/areadetector-1-9-1.git
/epics/src/areadetector-1-9-1  
RUN cd /epics/src/areadetector-1-9-1 && make -s -j4 all  
  
# Clone the sim IOC with simulated motors/areadetectors  
RUN git clone https://github.com/klauer/simioc.git /epics/iocs/simioc  
RUN cd /epics/iocs/simioc && make -s all  
  
# Clone the pyepics testIOC for its test suite  
RUN git clone https://github.com/pyepics/testioc /epics/iocs/pyepics_testioc  
RUN cd /epics/iocs/pyepics_testioc && make -s all  
  
# flash the neighbors  
EXPOSE 5064 5065  
# Stay root so that we can start system processes in server extensions.  
USER root  
RUN rm -rf extensions setup.py  
RUN apt-get install -yq supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  

