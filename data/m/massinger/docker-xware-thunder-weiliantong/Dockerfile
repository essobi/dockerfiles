FROM resin/armv7hf-debian  
  
RUN [ "cross-build-start" ]  
  
ADD Xware1.0.31_armel_v5te_glibc.tar.gz /opt/xware/  
  
WORKDIR /lib  
  
RUN ln -s ld-linux-armhf.so.3 ld-linux.so.3  
  
RUN apt-get update && \  
apt-get install -y libc6 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /opt/xware/  
VOLUME /opt/download/  
  
COPY run.sh /opt/xware/  
  
CMD ["bash", "/opt/xware/run.sh"]  
  
RUN [ "cross-build-end" ]  

