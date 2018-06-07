# base debian docker image that contains QEMU and scripts for running armhf
binaries  
FROM resin/armv7hf-debian:stretch  
  
LABEL io.resin.device-type="raspberrypi3"  
  
# required to execute commands via QEMU  
RUN [ "cross-build-start" ]  
  
# install supervisor deps  
RUN apt-get update && \  
apt-get install -y --no-install-recommends nmap jq && \  
rm -rf /var/lib/apt/lists/*  
  
# copy in launch script  
COPY ./entrypoint.sh /entrypoint.sh  
  
# make the script executable  
RUN chmod +x /entrypoint.sh  
  
# execute the entrypoint on boot  
CMD [ "/entrypoint.sh" ]  
  
RUN [ "cross-build-end" ]  

