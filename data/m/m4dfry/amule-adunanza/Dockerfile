FROM debian:jessie-slim  
ENV DEPENDENCIES="libcrypto++9 libupnp6"  
ENV DPKG_WXBASE_DEP="libexpat1"  
ENV DPKG_DAEMON_DEP="libpng12-0"  
# Add bin file  
ADD bin/* /setup/bin/  
ADD config/* /setup/config/  
ADD run.sh /usr/bin/run.sh  
  
RUN apt-get -y update && \  
apt-get install -y $DEPENDENCIES $DPKG_WXBASE_DEP $DPKG_DAEMON_DEP && \  
apt-get clean  
  
RUN dpkg -i /setup/bin/libwxbase2.8-0_2.8.12.1+dfsg-2ubuntu2_amd64.deb  
RUN dpkg -i /setup/bin/amule-adunanza-
daemon_2012.1+2.3.1~dfsg1-0ubuntu1_amd64.deb  
  
EXPOSE 4711/tcp 4712/tcp 4672/udp 4665/udp 4662/tcp 4661/tcp  
  
RUN chmod +x /usr/bin/run.sh  
CMD /usr/bin/run.sh  

