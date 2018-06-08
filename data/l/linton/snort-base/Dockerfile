# Snort in Docker  
FROM ubuntu:14.04.4  
MAINTAINER John Lin <linton.tw@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
wget \  
build-essential \  
# Pre-requisites for Snort DAQ (Data AcQuisition library)  
bison \  
flex \  
# Pre-Requisites for snort  
libpcap-dev \  
libpcre3-dev \  
libdumbnet-dev \  
# Additional required pre-requisite for Snort  
zlib1g-dev \  
# Optional libraries that improves fuctionality  
liblzma-dev \  
openssl \  
libssl-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# Define working directory.  
WORKDIR /opt  
  
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
  
RUN ldconfig  
  
# ENV SNORT_RULES_SNAPSHOT 2972  
# ADD snortrules-snapshot-${SNORT_RULES_SNAPSHOT} /opt  
ADD mysnortrules /opt  
RUN mkdir -p /var/log/snort && \  
mkdir -p /usr/local/lib/snort_dynamicrules && \  
mkdir -p /etc/snort && \  
# mysnortrules rules  
cp -r /opt/rules /etc/snort/rules && \  
# Due to empty folder so mkdir  
mkdir -p /etc/snort/preproc_rules && \  
mkdir -p /etc/snort/so_rules && \  
cp -r /opt/etc /etc/snort/etc && \  
# touch /etc/snort/rules/local.rules && \  
touch /etc/snort/rules/white_list.rules /etc/snort/rules/black_list.rules  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /tmp/* /var/tmp/* \  
/opt/snort-${SNORT_VERSION}.tar.gz /opt/daq-${DAQ_VERSION}.tar.gz  
  
# Validate an installation  
CMD ["snort", "-V"]  

