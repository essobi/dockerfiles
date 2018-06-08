FROM ubuntu:14.04  
RUN apt-get update && apt-get -y install \  
wget \  
build-essential \  
bison \  
flex \  
libpcap-dev \  
libpcre3-dev \  
libdumbnet-dev \  
zlib1g-dev  
  
ENV DAQ_VERSION 2.0.6  
RUN wget https://www.snort.org/downloads/snort/daq-${DAQ_VERSION}.tar.gz \  
&& tar xvfz daq-${DAQ_VERSION}.tar.gz \  
&& cd daq-${DAQ_VERSION} \  
&& ./configure; make; make install  
  
ENV SNORT_VERSION 2.9.8.3  
RUN wget https://www.snort.org/downloads/snort/snort-${SNORT_VERSION}.tar.gz \  
&& tar xvfz snort-${SNORT_VERSION}.tar.gz \  
&& cd snort-${SNORT_VERSION} \  
&& ./configure; make; make install  
  
CMD snort  

