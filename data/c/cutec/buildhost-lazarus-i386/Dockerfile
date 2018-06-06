FROM 32bit/debian  
MAINTAINER Christian Ulrich  
RUN apt-get -y update && \  
apt-get -y install git sudo fpc fpc-source binutils build-essential zip unzip
wget libusb-dev libdbus-1-dev libsane-dev sqlite3 postgresql-client binutils
libgtk2.0-0 libgtk2.0-dev psmisc  
  
RUN apt-get clean && apt-get autoremove -y  
  
RUN echo "Downloading and installing Debians" && \  
cd /tmp && \  
wget
"https://netix.dl.sourceforge.net/project/lazarus/Lazarus%20Linux%20i386%20DEB/Lazarus%201.8.0/lazarus-
project_1.8.0-0_i386.deb" -O lazarus.deb  
RUN ls /tmp/* && \  
dpkg -i --force-depends /tmp/lazarus.deb  
  
RUN lazbuild --build-ide="Normal IDE"; exit 0  

