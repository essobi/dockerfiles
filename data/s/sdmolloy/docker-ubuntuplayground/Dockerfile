FROM ubuntu:17.10  
MAINTAINER sdmolloy@gmail.com  
  
RUN apt-get -y update && \  
apt-get -y install build-essential xterm man wget readline-common libreadline-
dev sudo unzip vim  
  
RUN mkdir tmp_epics && \  
cd tmp_epics && \  
wget -nv https://www.aps.anl.gov/epics/download/base/base-3.15.5.tar.gz && \  
wget -nv https://www.aps.anl.gov/epics/download/modules/asyn4-32.tar.gz && \  
cd ..  
  
RUN mkdir epics && \  
cd epics && \  
tar -zxf ../tmp_epics/base-3.15.5.tar.gz -C ./ && \  
ln -s /epics /usr/local && \  
ln -s /epics/base-3.15.5 /epics/base && \  
cd base && \  
make  
  
RUN mkdir /epics/modules && \  
tar -zxf /tmp_epics/asyn4-32.tar.gz -C /epics/modules/ && \  
ln -s /epics/modules/asyn4-32 /epics/modules/asyn && \  
cd /epics/modules/asyn && \  
sed -i 's/^IPAC/#IPAC/' configure/RELEASE && \  
sed -i 's/^SNCSEQ/#SNCSEQ/' configure/RELEASE && \  
sed -i 's/^EPICS_BASE.*/EPICS_BASE=\/usr\/local\/epics\/base/'
configure/RELEASE && \  
make  
  
COPY ./aliasContents.txt /root/.bash_aliases  

