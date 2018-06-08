FROM phusion/baseimage:0.9.17  
MAINTAINER Marius Storm-Olsen <mstormo@gmail.no>  
  
LABEL Description="Seismic Unix on a proper Ubuntu 14.04 LTS base"  
  
# Use /data as the persistant storage for seismic  
VOLUME ["/data"]  
  
# Download Seismic Unix, build it, and clean up tools and build artifacts  
# Also try to strip down the image as much as possible by purging APT caches  
RUN apt-get update && apt-get install -y \  
build-essential \  
libx11-dev \  
libxt6 libxt-dev \  
&& curl -o /root/cwp_su_all_44R0.tgz -SL
"ftp://ftp.cwp.mines.edu/pub/cwpcodes/cwp_su_all_44R0.tgz" \  
&& mkdir /root/cwp \  
&& tar zxf /root/cwp_su_all_44R0.tgz -C /root/cwp \  
&& rm /root/cwp_su_all_44R0.tgz \  
&& /bin/bash -c \  
'echo exit 0 > /root/cwp/src/license.sh \  
&& echo exit 0 > /root/cwp/src/mailhome.sh \  
&& echo exit 0 > /root/cwp/src/chkroot.sh \  
&& CWPROOT=/root/cwp PATH=$PATH:/root/cwp/bin make -C /root/cwp/src install
xtinstall' \  
&& rm -rf /root/cwp/src \  
&& apt-get remove -y \  
build-essential \  
libx11-dev \  
libxt-dev \  
curl \  
&& rm -rf /var/lib/apt/lists \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y  
  
# Add trampoline which will sett CWPROOT for each command being called  
COPY trampoline.sh /root/cwp/trampoline.sh  
RUN chmod 755 /root/cwp/trampoline.sh  
  
# Symlink the trampoline script for every command in SU to /usr/local/bin  
# Since /usr/local/bin is already in path, it simplifies the commands from the
docker command line  
# docker run <image> segyread  
# instead of  
# docker run <image> /root/cwp/bin/segyread  
RUN cd /usr/local/bin/ \  
&& for f in /root/cwp/bin/*; do \  
ln -s /root/cwp/trampoline.sh `basename $f`; \  
done  

