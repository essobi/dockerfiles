FROM lnls/docker-epics-dev  
  
RUN apt-get update && \  
apt-get install -y libpcre3-dev  
  
RUN mkdir /opt/epics/stream && \  
cd /opt/epics/stream && \  
/opt/epics/base/bin/linux-x86_64/makeBaseApp.pl -t support -u janito && \  
sed -i -e ' \  
/DIRS :=/ h; \  
/DIRS :=/! { \  
t reset_condition_flag; \  
:reset_condition_flag; \  
x; \  
s/DIRS :=.*/DIRS := $(DIRS) streamDevice/; \  
t replaced; \  
b didnt_replace; \  
:replaced; \  
p; \  
s/.*//; \  
:didnt_replace; \  
x; \  
}' Makefile && \  
sed -i -e '/#SNCSEQ=/ { \  
p; \  
s,.*,,p; \  
s,.*,SUPPORT = /opt/epics/synApps_5_8/support,p; \  
s,.*,ASYN = $(SUPPORT)/asyn-4-26,p; \  
s,.*,CALC = $(SUPPORT)/calc-3-4-2-1,p; \  
s,.*,SSCAN = $(SUPPORT)/sscan-2-10-1,p; \  
}' configure/RELEASE && \  
echo 'PCRE_INCLUDE = /usr/include/pcre' >
configure/RELEASE.Common.linux-x86_64 && \  
echo 'PCRE_LIB = /usr/lib' >> configure/RELEASE.Common.linux-x86_64 && \  
git clone https://github.com/paulscherrerinstitute/StreamDevice.git
streamDevice && \  
cd streamDevice && \  
git checkout stream_2_7_7 && \  
rm GNUmakefile && \  
cd .. && \  
make install  
  
RUN cd /opt/epics/synApps_5_8/support && \  
sed -i -e 's|^STREAM=.*|STREAM=/opt/epics/stream|' configure/RELEASE && \  
sed -i -e 's|^STREAM=.*|STREAM=/opt/epics/stream|'
delaygen-1-1-1/configure/RELEASE && \  
export PATH=$PATH:/opt/epics/extensions/bin/linux-x86_64 && \  
make clean uninstall install  

