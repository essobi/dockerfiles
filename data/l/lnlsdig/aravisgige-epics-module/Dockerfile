FROM lnls/epics-dist:base-3.15-debian-9  
  
RUN apt-get update && \  
apt-get install -y \  
intltool \  
libgirepository1.0-dev \  
gtk-doc-tools \  
libglib2.0-dev \  
libglibmm-2.4-dev  
  
RUN git clone https://github.com/lnls-dig/aravis.git /opt/aravis && \  
cd /opt/aravis && \  
git checkout ARAVIS_0_4_1-LNLS1 && \  
./autogen.sh && \  
make distclean  
  
RUN git clone https://github.com/lnls-dig/aravisGigE /opt/epics/aravisGigE &&
\  
cd /opt/epics/aravisGigE && \  
git checkout R2-1-LNLS1 && \  
echo 'EPICS_BASE=/opt/epics/base' > configure/RELEASE.local && \  
echo 'SUPPORT=/opt/epics/synApps-lnls-R0-0-2/support' >>
configure/RELEASE.local && \  
echo 'AREADETECTOR=$(SUPPORT)/areaDetector-R3-2' >> configure/RELEASE.local &&
\  
echo 'ADCORE=$(AREADETECTOR)/ADCore' >> configure/RELEASE.local && \  
echo 'ASYN=$(SUPPORT)/asyn-R4-33' >> configure/RELEASE.local && \  
echo 'GLIBPREFIX=/usr' >> configure/RELEASE.local && \  
echo 'GLIB_INC1=/usr/lib/x86_64-linux-gnu/glib-2.0/include' >>
configure/RELEASE.local && \  
echo 'GLIB_INC2=/usr/lib/x86_64-linux-gnu/glib-2.0/include' >>
configure/RELEASE.local && \  
sed -i '/USR_LIBS += glib-2.0/c\USR_SYS_LIBS += glib-2.0'
aravisGigEApp/src/Makefile && \  
ln -s /opt/aravis vendor && \  
make  

