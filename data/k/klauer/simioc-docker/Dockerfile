FROM debian:jessie  
  
MAINTAINER NSLS-II <https://nsls-ii.github.io>  
  
USER root  
  
# Install the EPICS stack  
RUN apt-get -q update  
RUN apt-get install -yq wget  
RUN wget --quiet http://epics.nsls2.bnl.gov/debian/repo-key.pub -O - | apt-key
add -  
RUN echo "deb http://epics.nsls2.bnl.gov/debian/ jessie/staging main contrib"
| tee /etc/apt/sources.list.d/nsls2.list  
RUN apt-get update  
RUN apt-get install -yq build-essential git epics-dev epics-synapps-dev epics-
iocstats-dev  
RUN apt-get install -yq procserv telnet  
# get areadetector dependencies  
RUN apt-get install -yq libhdf5-dev libx11-dev libxext-dev libxml2-dev
libpng12-dev libbz2-dev libfreetype6-dev  
  
# clone and build EPICS device simulation code  
RUN mkdir /epics && mkdir /epics/iocs  
RUN mkdir /epics/src  
RUN git clone https://github.com/dchabot/areadetector-1-9-1.git
/epics/src/areadetector-1-9-1  
RUN cd /epics/src/areadetector-1-9-1 && make -s all  
  
RUN git clone https://github.com/dchabot/simioc /epics/iocs/simioc  
RUN git clone https://github.com/pyepics/testioc /epics/iocs/pyepics_testioc  
RUN cd /epics/iocs/simioc && make -s all  
  
# Load the pyepics testioc database file just before iocInit  
RUN sed -i '/^iocInit/ i
dbLoadRecords("/epics/iocs/pyepics_testioc/testiocApp/Db/pydebug.db",
"P=Py:")' /epics/iocs/simioc/iocBoot/ioclocalhost/st.cmd  
  
RUN apt-get install -yq python3 python3-pip python3-numpy  
# dependency dragged in from (at least) ophyd.commands  
RUN pip3 install https://github.com/pyepics/pyepics/zipball/master#egg=pyepics  
  
EXPOSE 5064 5065/udp  
  
# run simioc under supervisord (and procServ)  
RUN apt-get install -yq supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]  

