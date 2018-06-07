  
FROM debian:latest  
MAINTAINER FastFreddi  
  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y mono-vbnc libmono-system-web4.0.cil libmono-system-
design4.0.cil \  
libmono-system-web-extensions4.0-cil libmono-system-runtime-caching4.0-cil
flite chromium curl \  
libmono-system-data-datasetextensions4.0-cil libmono-system-xml-linq4.0-cil
mono-complete sudo wget vim screen && \  
apt-get update -y && apt-get clean  
  
# HomeSeer Install  
RUN wget http://homeseer.com/updates3/hs3_linux_3_0_0_312.tar.gz && \  
tar xvf hs3_linux_3_0_0_312.tar.gz -C /usr/local && rm
hs3_linux_3_0_0_312.tar.gz  
  
CMD su root && cd /usr/local/HomeSeer && ./go  

