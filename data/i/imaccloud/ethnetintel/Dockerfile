FROM node:5.11.0  
MAINTAINER "Kyle Bai <kyle.b@inwinstack.com>"  
# Install dependency packages  
RUN apt-get update && \  
apt-get install -y make g++ git  
  
# Install eth-netstats  
RUN cd /opt && \  
git clone https://github.com/cubedro/eth-net-intelligence-api ethnetintel && \  
cd ethnetintel && \  
npm install && npm install -g pm2  
  
COPY scripts/netstatconf.sh /opt/ethnetintel/netstatconf.sh  
COPY scripts/boot_run.sh /etc/boot_run.sh  
RUN chown root.root /etc/boot_run.sh && chmod 700 /etc/boot_run.sh  
  
WORKDIR /opt/ethnetintel  
  
# Show expose port  
EXPOSE 30303/tcp 30303/udp  
  
ENTRYPOINT ["/etc/boot_run.sh"]  

