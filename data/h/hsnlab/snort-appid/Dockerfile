# Snort in Docker  
FROM ubuntu:14.04.4  
MAINTAINER Rex5207 <abab5207@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
wget \  
build-essential \  
libpcap-dev \  
libpcre3-dev \  
libdumbnet-dev \  
bison \  
flex \  
zlib1g-dev \  
liblzma-dev \  
libluajit-5.1-dev \  
pkg-config \  
openssl \  
libssl-dev \  
vim && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir ~/snort_src  
  
# Define working directory.  
WORKDIR /snort_src  
  
ENV DAQ_VERSION 2.0.6  
RUN wget https://www.snort.org/downloads/snort/daq-${DAQ_VERSION}.tar.gz \  
&& tar xvfz daq-${DAQ_VERSION}.tar.gz \  
&& cd daq-${DAQ_VERSION} \  
&& ./configure; make; make install  
  
ENV SNORT_VERSION 2.9.9.0  
RUN wget https://www.snort.org/downloads/snort/snort-${SNORT_VERSION}.tar.gz \  
&& tar xvfz snort-${SNORT_VERSION}.tar.gz \  
&& cd snort-${SNORT_VERSION} \  
&& ./configure --enable-sourcefire --enable-open-appid; make; make install  
  
ENV APPID_VERSION 5048  
RUN wget https://snort.org/downloads/openappid/${APPID_VERSION} -O snort-
openappid.tar.gz \  
&& tar -xvzf snort-openappid.tar.gz  
  
RUN ldconfig  
  
RUN ln -s /usr/local/bin/snort /usr/sbin/snort  
  
# Create the Snort directories:  
RUN mkdir /etc/snort  
RUN mkdir /etc/snort/rules  
RUN mkdir /etc/snort/rules/iplists  
RUN mkdir /etc/snort/preproc_rules  
RUN mkdir /usr/local/lib/snort_dynamicrules  
RUN mkdir /etc/snort/so_rules  
  
# Create some files that stores rules and ip lists  
RUN touch /etc/snort/rules/iplists/black_list.rules  
RUN touch /etc/snort/rules/iplists/white_list.rules  
RUN touch /etc/snort/rules/local.rules  
RUN touch /etc/snort/sid-msg.map  
  
# Create our logging directories:  
RUN mkdir /var/log/snort  
RUN mkdir /var/log/snort/archived_logs  
  
# Adjust permissions:  
RUN chmod -R 5775 /etc/snort  
RUN chmod -R 5775 /var/log/snort  
RUN chmod -R 5775 /var/log/snort/archived_logs  
RUN chmod -R 5775 /etc/snort/so_rules  
RUN chmod -R 5775 /usr/local/lib/snort_dynamicrules  
  
RUN cp -r odp/ /etc/snort/rules/  
RUN mkdir /usr/local/lib/thirdparty  
  
ADD SnortRules /etc/snort/  
  
RUN apt-get clean && rm -rf /tmp/* /var/tmp/* \  
/snort_src/snort-${SNORT_VERSION}.tar.gz \  
/snort_src/daq-${DAQ_VERSION}.tar.gz \  
/snort_src/snort-openappid.tar.gz  

