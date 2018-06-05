FROM lnls/epics-dist  
  
RUN apt-get update && \  
apt-get install -y \  
intltool \  
libgirepository1.0-dev \  
gtk-doc-tools \  
libglib2.0-dev \  
libglibmm-2.4-dev  
  
RUN git clone https://github.com/lnls-dig/aravis.git /opt/aravis && \  
cd /opt/aravis && \  
git checkout bd182447a5dbc2041a9572a347de12ed95ce15e5 && \  
./autogen.sh && \  
make distclean  
  
RUN git clone https://github.com/lnls-dig/aravisGigE /opt/epics/aravisGigE &&
\  
cd /opt/epics/aravisGigE && \  
git checkout 3f17142763df1880ba2af11f6406df43dfb9f4dc && \  
echo 'EPICS_BASE=/opt/epics/base' > configure/RELEASE.local && \  
echo 'SUPPORT=/opt/epics/synApps_5_8/support' >> configure/RELEASE.local && \  
echo 'AREADETECTOR=$(SUPPORT)/areaDetector-R2-0' >> configure/RELEASE.local &&
\  
echo 'ADCORE=$(AREADETECTOR)/ADCore-R2-2' >> configure/RELEASE.local && \  
echo 'ASYN=$(SUPPORT)/asyn-4-26' >> configure/RELEASE.local && \  
echo 'GLIBPREFIX=/usr' >> configure/RELEASE.local && \  
echo 'GLIB_INC1=/usr/lib/x86_64-linux-gnu/glib-2.0/include' >>
configure/RELEASE.local && \  
echo 'GLIB_INC2=/usr/lib/x86_64-linux-gnu/glib-2.0/include' >>
configure/RELEASE.local && \  
ln -s /opt/aravis vendor && \  
make  
  
RUN cd /opt/epics/aravisGigE/iocs/aravisGigEIOC && \  
echo '-include $(ARAVISGIGE)/configure/RELEASE.local' >
configure/RELEASE.local && \  
echo >> configure/RELEASE.local && \  
echo 'CALC=$(SUPPORT)/calc-3-4-2-1' >> configure/RELEASE.local && \  
echo 'BUSY=$(SUPPORT)/busy-1-6-1' >> configure/RELEASE.local && \  
echo 'SSCAN=$(SUPPORT)/sscan-2-10-1' >> configure/RELEASE.local && \  
echo 'AUTOSAVE=$(SUPPORT)/autosave-5-6-1' >> configure/RELEASE.local && \  
echo >> configure/RELEASE.local && \  
echo 'HDF5_LIB = /usr/lib/x86_64-linux-gnu/hdf5/serial' >>
configure/RELEASE.local && \  
echo 'HDF5_INCLUDE = -I/usr/include/hdf5/serial' >> configure/RELEASE.local &&
\  
echo >> configure/RELEASE.local && \  
echo 'SZIP_LIB = /usr/lib' >> configure/RELEASE.local && \  
echo 'SZIP_INCLUDE =' >> configure/RELEASE.local && \  
make  

